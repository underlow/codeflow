# CodeFlow skills

Development guidance for Claude Code and Codex. The `flow` skill shares phase,
review, and resume rules, with small platform entrypoints for invocation and
native subagent tools.

Install for your user account with one command, without cloning the repository:

```sh
curl -fsSL https://raw.githubusercontent.com/underlow/codeflow/main/install-remote.sh | sh
```

The bootstrap script downloads the `main` archive to a temporary directory,
runs the installer, and removes the archive afterwards. To add the optional
`work-with-codex` skill or replace an existing installation, pass the same
options to `sh`:

```sh
curl -fsSL https://raw.githubusercontent.com/underlow/codeflow/main/install-remote.sh | sh -s -- --with-collab --force
```

If you already have the repository locally, run:

```sh
./install.sh
```

This copies `flow` to `~/.claude/skills/flow` and `~/.agents/skills/flow`.
Invoke it as `/flow [plan-folder-or-description-file]` in Claude Code or
`$flow [plan-folder-or-description-file]` in Codex. Codex discovers local skills
from `.agents/skills`; `.codex` holds its configuration and rules.

The separate `work-with-codex` skill uses Ghostty on macOS and installs a Codex
sender plus a rule allowing that sender to contact Claude. Install it explicitly:

```sh
./install.sh --with-collab --force
```

Use `--force` to replace an existing installation. The command above updates an
already installed `flow` while adding `work-with-codex`. `--target DIR` installs into
another home directory, which is useful for trying the installer without
changing your own setup. See [work-with-codex details](docs/work-with-codex.md).

The source layout is `skills/flow/shared/` for common instructions,
and `skills/flow/{claude,codex}/SKILL.md` for the platform entrypoints. When a
platform needs hooks or other files, add them to its platform directory and
the installer will copy them with its entrypoint.

The profiles are `full`, `medium`, `small`, and `bugfix`. See the
[phase guide](skills/flow/shared/references/phases.md). The detailed
[prompt library](skills/flow/shared/references/prompt-map.md) preserves the
original analysis, planning, implementation, and review criteria. The skill
does not require the former CodeFlow application.
