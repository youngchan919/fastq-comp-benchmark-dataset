import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CatalogueAndDownloader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load('download_benchmark')

    def test_manifest_and_plan_parity(self):
        jobs = self.module.select_jobs(None, 'data')
        self.assertEqual(len(jobs), 115)
        self.assertEqual(sum(x['size'] for x in jobs), 1419456345104)
        self.assertEqual(sum(bool(x['md5']) for x in jobs), 73)
        self.assertEqual(len({x['path'] for x in jobs}), 115)
        data8 = self.module.select_jobs('8', 'data')
        self.assertEqual(len(data8), 1)
        self.assertEqual(data8[0]['filename'], 'WY_reads.fq.gz')
        self.assertEqual(data8[0]['size'], 130270589600)
        self.assertEqual(data8[0]['md5'], '')
        self.assertEqual(len(self.module.select_jobs('10,30', 'data')), 4)
        self.assertEqual(len(self.module.select_jobs(None, 'references')), 18)
        with self.assertRaises(ValueError):
            self.module.select_jobs('28', 'data')

    def test_dry_run_does_not_create_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / 'not-created'
            with patch('sys.stdout', new_callable=io.StringIO), patch('sys.stderr', new_callable=io.StringIO):
                self.assertEqual(self.module.main(['--ids', '8', '--dry-run', '--output', str(destination)]), 0)
            self.assertFalse(destination.exists())

    def test_synthetic_verification_and_completed_partial(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = b'@toy\nACGT\n+\nIIII\n'
            path = root / 'toy.fastq'
            path.write_bytes(data)
            job = dict(path='data/Data_999/toy.fastq', filename='toy.fastq', kind='data',
                       url='https://example.invalid/not-requested', size=len(data), md5=hashlib.md5(data).hexdigest())
            downloader = self.module.Downloader(root, 0)
            self.assertEqual(downloader.verify(job, path), 'publisher-md5+size')
            self.assertEqual(downloader.verify(dict(job, md5=''), path), 'size-only')
            with self.assertRaises(ValueError):
                downloader.verify(dict(job, md5='0' * 32), path)
            partial = root / (job['path'] + '.part')
            partial.parent.mkdir(parents=True)
            partial.write_bytes(data)
            with patch.object(self.module.subprocess, 'Popen', side_effect=AssertionError('No network allowed in test')):
                result = downloader.one(job)
            self.assertEqual(result['status'], 'downloaded')
            self.assertEqual((root / job['path']).read_bytes(), data)
            self.assertFalse(partial.exists())

    def test_synthetic_checksum_failure_preserves_partial(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            job = dict(path='toy.gz', filename='toy.gz', kind='data', size=4,
                       md5='0' * 32, url='https://example.invalid/not-requested')
            partial = root / 'toy.gz.part'
            partial.write_bytes(b'test')
            result = self.module.Downloader(root, 0).one(job)
            self.assertEqual(result['status'], 'failed')
            self.assertEqual(partial.read_bytes(), b'test')
            self.assertFalse((root / 'toy.gz').exists())

    def test_synthetic_reference_header_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'reference.fa.gz'
            with gzip.open(path, 'wb') as handle:
                handle.write(b'>toy\nACGT\n')
            job = dict(kind='reference', filename=path.name, size=None, md5='')
            self.assertEqual(self.module.Downloader(Path(tmp), 0).verify(job, path), 'FASTA-header-only')


class SyntheticExport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load('prepare_data6')
        if subprocess.check_output(['samtools', '--version-only'], text=True).strip() != cls.module.PINNED_VERSION:
            raise unittest.SkipTest('Pinned samtools/htslib 1.22 is required for export tests')

    def make_bam(self, root, records):
        sam = root / 'toy.sam'
        sam.write_text('@HD\tVN:1.6\tSO:unsorted\n@SQ\tSN:chr1\tLN:100\n' + '\n'.join(records) + '\n')
        bam = root / 'toy.bam'
        subprocess.run(['samtools', 'view', '-b', '-o', str(bam), str(sam)], check=True)
        return bam

    def test_exact_order_orientation_qualities_and_filtering(self):
        records = [
            'read10\t4\t*\t0\t0\t*\t*\t0\t0\tNNAC\tJJJJ',
            'read2\t16\tchr1\t5\t60\t4M\t*\t0\t0\tAGTC\tJKLM',
            'read1\t0\tchr1\t1\t60\t4M\t*\t0\t0\tACGT\tIIII\tOQ:Z:ZZZZ',
            'read1\t256\tchr1\t7\t60\t4M\t*\t0\t0\tACGT\tHHHH',
            'read2\t2048\tchr1\t10\t60\t4M\t*\t0\t0\tAGTC\tHHHH']
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bam = self.make_bam(root, records)
            receipt = self.module.prepare(bam, root / 'first')
            expected = b'@read1\nACGT\n+\nIIII\n@read2\nGACT\n+\nMLKJ\n@read10\nNNAC\n+\nJJJJ\n'
            self.assertEqual((root / 'first/Data_6.fastq').read_bytes(), expected)
            self.assertEqual(receipt['primary_records'], 3)
            self.assertEqual(receipt['missing_QUAL_records'], 0)
            second = self.module.prepare(bam, root / 'second')
            self.assertEqual(receipt['output_sha256'], second['output_sha256'])

    def test_missing_quality_is_not_synthesized(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bam = self.make_bam(root, ['missing\t4\t*\t0\t0\t*\t*\t0\t0\tACGT\t*'])
            with self.assertRaisesRegex(ValueError, 'Missing primary QUAL'):
                self.module.prepare(bam, root / 'out')
            self.assertFalse((root / 'out/Data_6.fastq').exists())

    def test_unexpected_pairing_is_not_silently_dropped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bam = self.make_bam(root, ['paired\t65\tchr1\t1\t60\t4M\t*\t0\t0\tACGT\tIIII'])
            with self.assertRaisesRegex(ValueError, 'paired'):
                self.module.prepare(bam, root / 'out')
            self.assertFalse((root / 'out/Data_6.fastq').exists())

    def test_duplicate_primary_name_is_not_silently_dropped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bam = self.make_bam(root, ['duplicate\t0\tchr1\t1\t60\t4M\t*\t0\t0\tACGT\tIIII'] * 2)
            with self.assertRaisesRegex(ValueError, 'Duplicate'):
                self.module.prepare(bam, root / 'out')
            self.assertFalse((root / 'out/Data_6.fastq').exists())


if __name__ == '__main__':
    unittest.main()
