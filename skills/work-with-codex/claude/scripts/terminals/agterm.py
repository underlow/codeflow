import shlex
from . import run


class Agterm:
    def __init__(self, env):
        self.origin = env['AGTERM_SESSION_ID']
        self.options = ['--socket', env['AGTERM_SOCKET'], '--window', env['AGTERM_WINDOW_ID']]
        self.pane = (['--pane-id', env['AGTERM_PANE_ID']] if env.get('AGTERM_PANE_ID')
                     else ['--pane', env.get('AGTERM_PANE', 'left')])

    def start(self, command, cwd):
        return run('agtermctl', 'session', 'new', '--after', self.origin, '--cwd', str(cwd),
                   '--name', 'Codex', '--command', command, '--no-select', *self.options)

    def commands(self, target, agent):
        pane = self.pane if target == self.origin else []
        send = shlex.join(['agtermctl', 'session', 'type', '--target', target, *pane, *self.options, '--stdin'])
        send = "printf '\\033[200~%s\\033[201~\\r' MESSAGE | " + send
        close = shlex.join(['agtermctl', 'session', 'close', '--target', target, *self.options])
        return send, close
