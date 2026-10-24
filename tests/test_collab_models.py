"""Model resolution and failed-start behavior, without launching a model or UI."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'skills/work-with-codex/claude/scripts'
spec = importlib.util.spec_from_file_location('resolve_model', SCRIPTS / 'resolve-model.py')
resolver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resolver)
MODELS = [
    {'slug': 'test-v2-sol', 'display_name': 'Sol v2', 'visibility': 'list',
     'supported_reasoning_levels': [{'effort': 'low'}, {'effort': 'high'}]},
    {'slug': 'test-v1-sol', 'display_name': 'Sol v1', 'visibility': 'list',
     'supported_reasoning_levels': [{'effort': 'low'}]},
]


class ModelResolutionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='collab-models-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.aliases = self.root / 'aliases.json'
        self.aliases.write_text(json.dumps({'sol': 'test-v2-sol'}))
        self.codex = self.root / 'codex'
        self.codex.write_text('#!' + sys.executable + '\nimport json,sys\n'
                              'assert sys.argv[1:3] == ["debug", "models"]\n'
                              'print(' + repr(json.dumps({'models': MODELS})) + ')\n')
        self.codex.chmod(0o755)

    def cli(self, model, *options):
        return subprocess.run([
            sys.executable, str(SCRIPTS / 'resolve-model.py'),
            '--codex', str(self.codex), '--aliases', str(self.aliases),
            *options, model,
        ], text=True, capture_output=True, timeout=5)

    def test_alias_case_and_effort(self):
        result = self.cli('Sol', '--effort', 'high')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), 'test-v2-sol')

    def test_exact_id_and_display_name(self):
        for name in ['test-v1-sol', 'sOL V1']:
            self.assertEqual(self.cli(name).stdout.strip(), 'test-v1-sol')

    def test_unknown_name_returns_choices(self):
        result = self.cli('unknown')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('test-v2-sol', result.stderr)
        self.assertIn('test-v1-sol', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_stale_alias_does_not_choose_another_generation(self):
        self.aliases.write_text('{"sol":"removed-model"}')
        result = self.cli('sol')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('removed-model', result.stderr)
        self.assertIn('test-v2-sol', result.stderr)

    def test_invalid_effort_and_config_return_choices(self):
        result = self.cli('sol', '--effort', 'ultra')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('does not support effort', result.stderr)
        self.assertIn('test-v1-sol', result.stderr)
        self.aliases.write_text('{broken')
        result = self.cli('sol')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Available catalog models', result.stderr)

    def test_bundled_fallback(self):
        source = self.codex.read_text()
        self.codex.write_text(source.replace('print(',
            'if "--bundled" not in sys.argv: sys.exit(1)\nprint(', 1))
        result = self.cli('sol')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('bundled catalog', result.stderr)

    def test_start_failure_precedes_terminal_setup(self):
        environment = dict(os.environ, PATH=str(self.root) + os.pathsep + os.environ['PATH'])
        environment['HOME'] = str(self.root)
        result = subprocess.run([
            sys.executable, str(SCRIPTS / 'collab.sh'), 'start',
            '--model', 'unknown', '--effort', 'high', str(self.root),
        ], input='brief', text=True, capture_output=True, env=environment, timeout=5)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Available catalog models', result.stderr)
        self.assertNotIn('inbox socket', result.stderr)
        self.assertNotIn('ID ', result.stdout)

    def test_start_validates_model_before_reading_brief(self):
        environment = dict(os.environ, PATH=str(self.root) + os.pathsep + os.environ['PATH'])
        environment['HOME'] = str(self.root)
        result = subprocess.run([
            sys.executable, str(SCRIPTS / 'collab.sh'), 'start',
            '--model', 'test-v2-sol', '--effort', 'high', str(self.root),
        ], input='', text=True, capture_output=True, env=environment, timeout=5)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('model test-v2-sol -> test-v2-sol', result.stderr)
        self.assertIn('brief expected on stdin', result.stderr)
        self.assertNotIn('ID ', result.stdout)


if __name__ == '__main__':
    unittest.main()
