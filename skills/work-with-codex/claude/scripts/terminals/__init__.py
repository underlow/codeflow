"""Find the originating terminal, without selecting a window or tab."""
import os
from pathlib import Path
import subprocess


def run(*command):
    return subprocess.run(command, text=True, capture_output=True, check=True).stdout.strip()


from .agterm import Agterm
from .cmux import Cmux
from .ghostty import Ghostty


def detect():
    env = os.environ
    if env.get('AGTERM_ENABLED') == '1' or env.get('TERM_PROGRAM') == 'agterm':
        return Agterm(env)
    if env.get('CMUX_SURFACE_ID') or env.get('TERM_PROGRAM') == 'cmux':
        return Cmux(env)
    pid = Path(env.get('CLAUDE_CODE_MESSAGING_SOCKET', '')).stem
    pid = int(pid) if pid.isdigit() else os.getppid()
    while pid > 1:
        parent, tty = run('ps', '-o', 'ppid=', '-o', 'tty=', '-p', str(pid)).split()
        if tty not in ('?', '??'):
            return Ghostty('/dev/' + tty)
        pid = int(parent)
    raise ValueError('cannot find the originating terminal')
