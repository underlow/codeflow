#!/usr/bin/env python3
"""Start Codex and print native terminal commands for the conversation."""
import argparse
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys

from terminals import detect

skill = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('action', choices=['start'])
parser.add_argument('--task', choices=['discuss', 'develop', 'review'],
                    default='develop' if skill.name == 'delegate-to-codex' else 'discuss')
parser.add_argument('--model')
parser.add_argument('--effort')
parser.add_argument('directory', nargs='?', default=os.getcwd())
args = parser.parse_intermixed_args()

try:
    if args.task != 'discuss' and not args.model:
        raise ValueError('delegation requires --model; ask the user which model to use')
    if skill.name == 'delegate-to-codex' and args.task == 'discuss':
        raise ValueError('delegation task must be develop or review')
    cwd = Path(args.directory).resolve()
    if not cwd.is_dir():
        raise ValueError(f'no directory {cwd}')
    binary = shutil.which('codex')
    if not binary:
        raise ValueError('codex is not on PATH')
    options = []
    if args.model:
        resolver = [sys.executable, str(skill / 'scripts/resolve-model.py'), '--codex', binary,
                    '--aliases', str(Path.home() / '.codex/collab/model-aliases.json')]
        if args.effort:
            resolver += ['--effort', args.effort]
        model = subprocess.run(resolver + [args.model], text=True, stdout=subprocess.PIPE, check=True).stdout.strip()
        options += ['--model', model]
        print(f'collab.sh: model {args.model} -> {model}', file=sys.stderr)
    if args.effort:
        options += ['-c', f'model_reasoning_effort="{args.effort}"']
    brief = sys.stdin.read().strip()
    if not brief:
        raise ValueError('brief expected on stdin')
    terminal = detect()
    reply, _ = terminal.commands(terminal.origin, 'claude')
    prompt = (skill / 'codex-prompt.md').read_text().replace('{{REPLY}}', reply)
    command = shlex.join(['/usr/bin/env', 'PATH=' + os.environ.get('PATH', os.defpath), binary,
                          '--sandbox', 'workspace-write' if args.task == 'develop' else 'read-only',
                          '--ask-for-approval', 'on-request', *options, 'Mode: ' + args.task + '\n' + prompt + '\n' + brief])
    target = terminal.start(command, cwd)
    send, close = terminal.commands(target, 'codex')
    print(f'ID {target}\nSEND {send}\nCLOSE {close}')
except subprocess.CalledProcessError as error:
    if error.stderr:
        print(error.stderr.strip(), file=sys.stderr)
    sys.exit(error.returncode)
except (OSError, ValueError, KeyError, StopIteration) as error:
    print(f'collab.sh: {error}', file=sys.stderr)
    sys.exit(1)
