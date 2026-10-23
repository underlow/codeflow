#!/usr/bin/env python3
"""Discover Claude peers, send messages, and retain replies across sessions."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import socket
import stat
import sys
import time
import uuid


def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))


def peers(registry):
    result = []
    for path in registry.glob('*.json'):
        try:
            peer = json.loads(path.read_text())
            address = Path(peer['messagingSocketPath'])
            if not stat.S_ISSOCK(address.stat().st_mode):
                continue
            if address.stat().st_uid != os.getuid():
                continue
            result.append({
                'session_id': peer['sessionId'], 'name': peer.get('name'),
                'project': peer.get('cwd'), 'status': peer.get('status'),
                'entrypoint': peer.get('entrypoint'), 'socket': str(address),
            })
        except (OSError, ValueError, KeyError, TypeError):
            continue
    return sorted(result, key=lambda peer: (peer.get('name') or '', peer['session_id']))


def find_peer(registry, session_id):
    matches = [peer for peer in peers(registry) if peer['session_id'] == session_id]
    if len(matches) != 1:
        raise ValueError('Selected Claude session is no longer available; list sessions again.')
    return matches[0]


def read_message():
    message = sys.stdin.read().strip()
    if not message:
        raise ValueError('Expected a nonempty message on stdin.')
    return message


def save_json(path, value):
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def connection_path(state, identifier):
    if len(identifier) != 24 or any(c not in '0123456789abcdef' for c in identifier):
        raise ValueError('Invalid connection ID.')
    return state / identifier


def reply_command(state, identifier):
    return shlex.join([
        sys.executable, str(Path(__file__).resolve()), '--state-dir', str(state),
        'reply', identifier,
    ])


def send_peer(peer, text):
    # Same local Claude inbox envelope used by work-with-codex/codex/collab.sh.
    payload = {'type': 'user', 'message': {'role': 'user', 'content': text}}
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.settimeout(3)
        client.connect(peer['socket'])
        client.sendall((json.dumps(payload, ensure_ascii=False) + '\n').encode())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry-dir', type=Path, default=Path.home() / '.claude/sessions')
    parser.add_argument('--state-dir', type=Path, default=Path.home() / '.cache/codeflow/talk-to-designer')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    bind = sub.add_parser('connect')
    bind.add_argument('session_id')
    bind.add_argument('--project', type=Path, default=Path.cwd())
    for command in ('send', 'reply', 'read', 'wait', 'history'):
        action = sub.add_parser(command)
        action.add_argument('connection')
        if command in ('read', 'wait'):
            action.add_argument('--after', default='')
        if command == 'wait':
            action.add_argument('--timeout', type=float, default=50)
    connections = sub.add_parser('connections')
    connections.add_argument('--project', type=Path, default=Path.cwd())
    args = parser.parse_args()
    state = args.state_dir.expanduser().resolve()

    if args.command == 'list':
        emit(peers(args.registry_dir))
        return
    if args.command == 'connections':
        result = []
        for path in state.glob('*/connection.json'):
            record = json.loads(path.read_text())
            if record['project'] == str(args.project.resolve()):
                result.append(record)
        emit(result)
        return
    if args.command == 'connect':
        peer = find_peer(args.registry_dir, args.session_id)
        project = str(args.project.resolve())
        identifier = hashlib.sha256((project + '\n' + args.session_id).encode()).hexdigest()[:24]
        directory = connection_path(state, identifier)
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        (directory / 'inbox').mkdir(exist_ok=True, mode=0o700)
        (directory / 'outbox').mkdir(exist_ok=True, mode=0o700)
        record = {
            'connection': identifier, 'project': project,
            'designer_session': peer['session_id'], 'designer_name': peer['name'],
            'caller_thread': os.environ.get('CODEX_THREAD_ID'),
            'reply_command': reply_command(state, identifier),
        }
        save_json(directory / 'connection.json', record)
        emit(record)
        return

    directory = connection_path(state, args.connection)
    record = json.loads((directory / 'connection.json').read_text())
    if args.command == 'send':
        text = read_message()
        peer = find_peer(args.registry_dir, record['designer_session'])
        send_peer(peer, text)
        identifier = '{:020d}-{}'.format(time.time_ns(), uuid.uuid4().hex[:8])
        save_json(directory / 'outbox' / (identifier + '.json'), {'id': identifier, 'text': text})
        emit({'sent': True, 'connection': args.connection, 'designer': peer['name']})
    elif args.command == 'reply':
        text = read_message()
        identifier = '{:020d}-{}'.format(time.time_ns(), uuid.uuid4().hex[:8])
        save_json(directory / 'inbox' / (identifier + '.json'), {'id': identifier, 'text': text})
        emit({'saved': True, 'id': identifier})
    elif args.command == 'history':
        messages = []
        for box, author in [('inbox', 'designer'), ('outbox', 'caller')]:
            for path in (directory / box).glob('*.json'):
                message = json.loads(path.read_text())
                messages.append(dict(message, author=author))
        emit(sorted(messages, key=lambda message: message['id']))
    else:
        timeout = min(55, max(0, args.timeout)) if args.command == 'wait' else 0
        deadline = time.monotonic() + timeout
        while True:
            replies = [json.loads(path.read_text()) for path in sorted((directory / 'inbox').glob('*.json'))
                       if path.stem > args.after]
            if replies or time.monotonic() >= deadline:
                emit({'connection': args.connection, 'replies': replies,
                      'cursor': replies[-1]['id'] if replies else args.after})
                break
            time.sleep(0.25)


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        print('designer: ' + str(error), file=sys.stderr)
        sys.exit(1)
