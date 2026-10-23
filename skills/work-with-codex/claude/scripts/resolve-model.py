#!/usr/bin/env python3
"""Resolve an explicit model against aliases and the launcher's Codex catalog."""

import argparse
import json
from pathlib import Path
import subprocess
import sys


def catalog(binary):
    for bundled in (False, True):
        command = [binary, 'debug', 'models'] + (['--bundled'] if bundled else [])
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=20)
            if result.returncode:
                continue
            data = json.loads(result.stdout)
            models = data['models']
            if not isinstance(models, list) or not models:
                continue
            if bundled:
                print('collab.sh: catalog refresh unavailable; checking against bundled catalog.', file=sys.stderr)
            return models
        except (OSError, ValueError, KeyError, subprocess.TimeoutExpired):
            continue
    raise ValueError('Cannot read the model catalog from this Codex binary; no session started.')


def choices(models):
    lines = ['Available catalog models (account access is checked by Codex at runtime):']
    for model in models:
        if model.get('visibility') != 'list':
            continue
        efforts = ', '.join(level['effort'] for level in model.get('supported_reasoning_levels', []))
        lines.append('  {} — {}{}'.format(model['slug'], model.get('display_name', model['slug']),
                                         ' (effort: {})'.format(efforts) if efforts else ''))
    return '\n'.join(lines)


def resolve(request, aliases, models, effort=None):
    # Exact IDs remain usable even when hidden from the normal picker.
    exact = [model for model in models if model.get('slug') == request]
    if exact:
        matches = exact
    elif request.casefold() in aliases:
        target = aliases[request.casefold()]
        matches = [model for model in models if model.get('slug') == target]
        if not matches:
            raise ValueError('Alias {!r} points to {!r}, which is absent from the catalog.'.format(request, target))
    else:
        matches = [model for model in models if model.get('visibility') == 'list' and
                   request.casefold() in (model.get('slug', '').casefold(),
                                          model.get('display_name', '').casefold())]
    if len(matches) != 1:
        raise ValueError('Cannot choose model {!r}: no unique match. Use an alias or exact catalog ID.'.format(request))
    selected = matches[0]
    if effort and effort not in [level['effort'] for level in selected.get('supported_reasoning_levels', [])]:
        raise ValueError('Model {} does not support effort {!r}.'.format(selected['slug'], effort))
    return selected['slug']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--codex', required=True)
    parser.add_argument('--aliases', type=Path, required=True)
    parser.add_argument('--effort')
    parser.add_argument('model')
    args = parser.parse_args()
    models = catalog(args.codex)
    try:
        aliases = json.loads(args.aliases.read_text()) if args.aliases.exists() else {}
        if not isinstance(aliases, dict) or any(not isinstance(k, str) or not isinstance(v, str)
                                               for k, v in aliases.items()):
            raise ValueError('Alias config must be a JSON object mapping names to exact model IDs.')
        normalized = {key.casefold(): value for key, value in aliases.items()}
        if len(normalized) != len(aliases):
            raise ValueError('Alias config contains names differing only in case.')
        selected = resolve(args.model, normalized, models, args.effort)
    except (OSError, ValueError) as error:
        print('collab.sh: {}\n{}\nAlias config: {}'.format(error, choices(models), args.aliases), file=sys.stderr)
        return 2
    print(selected)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except ValueError as error:
        print('collab.sh: ' + str(error), file=sys.stderr)
        sys.exit(2)
