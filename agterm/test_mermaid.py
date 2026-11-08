import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).parent / 'files/.config/agterm/scripts/mermaid-overlay.py'
spec = importlib.util.spec_from_file_location('mermaid_overlay', SCRIPT)
mermaid = importlib.util.module_from_spec(spec)
# The scripts directory is an installation payload; keep Python bytecode out of it.
with patch.object(sys, 'dont_write_bytecode', True):
    spec.loader.exec_module(mermaid)


class MermaidTests(unittest.TestCase):
    def test_selection_accepts_claude_header_and_markdown_fences(self):
        code = 'flowchart LR\n  A --> B'
        for selection in (code, 'mermaid\n' + code, '```mermaid\n' + code + '\n```',
                          '~~~mermaid\n' + code + '\n~~~'):
            self.assertEqual(mermaid.source_from_selection(selection), code)

    def test_empty_selection_requires_selection(self):
        for selection in ('', '  ', 'mermaid', '```mermaid\n```'):
            with self.assertRaises(ValueError):
                mermaid.source_from_selection(selection)

    def test_preserves_quotes_unicode_and_multiline_labels(self):
        code = 'flowchart LR\n  A["Сохранение\\nочереди"] --> B["a & b"]'
        self.assertEqual(mermaid.source_from_selection(code), code)

    def test_selection_cannot_inject_html_or_overlay_controls(self):
        source = '</pre><button data-agterm="session.close">x</button><script>alert(1)</script>'
        page = mermaid.page(source)
        self.assertNotIn(source, page)
        self.assertIn('&lt;/pre&gt;', page)
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;', page)

    def test_claude_selection_can_be_read_from_clipboard(self):
        with patch.dict(os.environ, {'AGT_SELECTION': ''}), \
             patch.object(mermaid.subprocess, 'run', return_value=subprocess.CompletedProcess(
                 [], 0, stdout='```mermaid\nflowchart LR\nA --> B\n```')):
            self.assertEqual(mermaid.selected_source(), 'flowchart LR\nA --> B')

    def test_native_selection_takes_priority_without_reading_clipboard(self):
        with patch.dict(os.environ, {'AGT_SELECTION': 'flowchart LR\nA --> B'}), \
             patch.object(mermaid.subprocess, 'run') as run:
            self.assertEqual(mermaid.selected_source(), 'flowchart LR\nA --> B')
            run.assert_not_called()

    def test_unrelated_clipboard_does_not_open_a_diagram(self):
        for text in ('', 'ordinary clipboard text', 'https://example.com'):
            with patch.dict(os.environ, {'AGT_SELECTION': ''}), \
                 patch.object(mermaid.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, stdout=text)):
                with self.assertRaises(ValueError):
                    mermaid.selected_source()

    def test_overlay_targets_origin_and_keeps_files_until_dismissed(self):
        def open_overlay(args, **kwargs):
            self.assertEqual(args[args.index('--target') + 1], 'origin-session')
            self.assertEqual(args[args.index('--socket') + 1], '/origin.sock')
            document = Path(args[args.index('--html') + 1])
            self.assertTrue(document.exists())
            self.assertTrue(document.with_name('mermaid.min.js').exists())
            self.assertIn('--block', args)
            self.document = document
            return subprocess.CompletedProcess(args, 2)

        with patch.dict(os.environ, {'AGT_SELECTION': 'flowchart LR\nA --> B',
                                     'AGT_SESSION_ID': 'origin-session', 'AGT_SOCKET': '/origin.sock'}), \
             patch.object(mermaid, 'library_path', return_value=SCRIPT), \
             patch.object(mermaid.subprocess, 'run', side_effect=open_overlay):
            mermaid.main()
        self.assertFalse(self.document.exists())


if __name__ == '__main__':
    unittest.main()
