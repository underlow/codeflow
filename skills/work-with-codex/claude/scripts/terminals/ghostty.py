from pathlib import Path
import shlex
from . import run

BRIDGE = str(Path(__file__).resolve().parents[1] / 'ghostty.applescript')


class Ghostty:
    def __init__(self, tty):
        self.origin, self.title = run('osascript', BRIDGE, 'identify', tty).split('\n', 1)

    def start(self, command, cwd):
        return run('osascript', BRIDGE, 'tab', self.origin, command, str(cwd), self.title)

    def commands(self, target, agent):
        return (shlex.join(['osascript', BRIDGE, 'send', target]) + ' MESSAGE',
                shlex.join(['osascript', BRIDGE, 'close', target]))
