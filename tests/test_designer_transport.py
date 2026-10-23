"""Exercise transport against an isolated Claude-compatible Unix inbox."""

import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/talk-to-designer/shared/scripts/designer.py'


class DesignerTransportTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='designer-', dir='/private/tmp')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.registry = self.root / 'registry'
        self.registry.mkdir()
        self.state = self.root / 'state'
        self.listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.addCleanup(self.listener.close)
        self.address = self.root / 'claude.sock'
        self.listener.bind(str(self.address))
        self.listener.listen(1)
        self.listener.settimeout(3)
        self.metadata = self.registry / '123.json'
        self.metadata.write_text(json.dumps({
            'sessionId': 'designer-test', 'name': 'Designer',
            'cwd': str(self.root), 'messagingSocketPath': str(self.address),
            'entrypoint': 'claude-desktop', 'status': 'idle',
        }))

    def run_script(self, *args, message=None, success=True):
        result = subprocess.run([
            sys.executable, str(SCRIPT), '--registry-dir', str(self.registry),
            '--state-dir', str(self.state), *args,
        ], input=message, text=True, capture_output=True, timeout=5)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        self.assertNotEqual(result.returncode, 0)
        return result

    def connect(self):
        return self.run_script('connect', 'designer-test', '--project', str(self.root))['connection']

    def test_discovery_send_and_reply_across_processes(self):
        self.assertEqual(self.run_script('list')[0]['name'], 'Designer')
        connection = self.connect()
        text = 'Дизайн: "кавычки", $HOME и `текст`\nВторая строка'
        self.run_script('send', connection, message=text)
        client, _ = self.listener.accept()
        with client:
            chunks = []
            while True:
                chunk = client.recv(4096)
                if not chunk:
                    break
                chunks.append(chunk)
        envelope = json.loads(b''.join(chunks))
        self.assertEqual(envelope, {'type': 'user', 'message': {'role': 'user', 'content': text}})
        self.run_script('reply', connection, message='Ответ дизайнера')
        result = self.run_script('read', connection)
        self.assertEqual(result['replies'][0]['text'], 'Ответ дизайнера')
        history = self.run_script('history', connection)
        self.assertEqual([item['author'] for item in history], ['caller', 'designer'])
        self.assertEqual(history[0]['text'], text)
        self.assertEqual(self.run_script('read', connection, '--after', result['cursor'])['replies'], [])
        self.assertEqual(self.connect(), connection)
        self.assertEqual(len(self.run_script('read', connection)['replies']), 1)
        saved = self.run_script('connections', '--project', str(self.root))
        self.assertEqual(saved[0]['connection'], connection)

    def test_wait_for_delayed_reply_and_timeout(self):
        connection = self.connect()
        def reply():
            time.sleep(0.2)
            self.run_script('reply', connection, message='Готово')
        worker = threading.Thread(target=reply)
        worker.start()
        result = self.run_script('wait', connection, '--timeout', '2')
        worker.join()
        self.assertEqual(result['replies'][0]['text'], 'Готово')
        pending = self.run_script('wait', connection, '--after', result['cursor'], '--timeout', '0.1')
        self.assertEqual(pending['replies'], [])

    def test_stale_session_and_invalid_connection(self):
        connection = self.connect()
        self.metadata.unlink()
        self.assertEqual(self.run_script('list'), [])
        self.run_script('send', connection, message='hello', success=False)
        self.run_script('read', '../escape', success=False)
        self.assertTrue(self.state.is_dir())


if __name__ == '__main__':
    unittest.main()
