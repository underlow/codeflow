import json
import shlex
from . import run


class Cmux:
    def __init__(self, env):
        self.origin = env['CMUX_SURFACE_ID']
        self.workspace = env['CMUX_WORKSPACE_ID']
        self.cli = ['cmux', '--socket', env.get('CMUX_SOCKET_PATH', '/tmp/cmux.sock')]

    def start(self, command, cwd):
        surfaces = json.loads(run(*self.cli, 'list-panels', '--workspace', self.workspace,
                                  '--json', '--id-format', 'uuids'))['surfaces']
        parent = next(row for row in surfaces if row['id'] == self.origin)
        result = run(*self.cli, 'new-surface', '--workspace', self.workspace, '--pane', parent['pane_id'],
                     '--cwd', str(cwd), '--command', command, '--focus', 'false', '--json', '--id-format', 'uuids')
        return json.loads(result)['surface_id']

    def commands(self, target, agent):
        if agent == 'claude':
            send = [*self.cli, 'agent', 'message', target, '--']
        else:
            send = [*self.cli, 'paste', '--workspace', self.workspace, '--surface', target, '--submit', '--']
        close = [*self.cli, 'close-surface', '--workspace', self.workspace, '--surface', target]
        return shlex.join(send) + ' MESSAGE', shlex.join(close)
