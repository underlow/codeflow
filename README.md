# CodeFlow skills

Development guidance for Claude Code and Codex. `flow` handles one change from
planning through review. `underlow/project` researches a larger idea, keeps an
evolving map of stages, and hands a chosen stage to a separate ordinary `flow`.
Both use shared instructions with small platform entrypoints.

Install for your user account with one command, without cloning the repository:

```sh
curl -fsSL https://raw.githubusercontent.com/underlow/codeflow/master/install-remote.sh | sh
```

The bootstrap script downloads the `master` archive to a temporary directory,
runs the installer, and removes the archive afterwards. To add the optional
`work-with-codex` skill or replace an existing installation, pass the same
options to `sh`:

```sh
curl -fsSL https://raw.githubusercontent.com/underlow/codeflow/master/install-remote.sh | sh -s -- --with-collab --force
```

If you already have the repository locally, run:

```sh
./install.sh
```

This copies `flow` and `project` to `~/.claude/skills/` and
`~/.agents/skills/`.
Invoke it as `/flow [plan-folder-or-description-file]` in Claude Code or
`$flow [plan-folder-or-description-file]` in Codex. Codex discovers local skills
from `.agents/skills`; `.codex` holds its configuration and rules.

To start or resume a larger project, use `/project [project-file]` in Claude
Code or `$project [project-file]` in Codex. The project skill saves research and
an editable stage map in `docs/projects/`. You choose a stage; it prepares a
short handoff file for a new `flow` session. The flow session chooses its own
profile with you and runs independently. Returning to `project` reconciles the
stage against its flow plan and Git history, or you can reconsider the overall
map at any time.

The separate `work-with-codex` skill uses Ghostty on macOS and installs a Codex
sender plus a rule allowing that sender to contact Claude. Install it explicitly:

```sh
./install.sh --with-collab --force
```

Use `--force` to replace an existing installation. The command above updates an
already installed `flow` while adding `work-with-codex`. `--target DIR` installs into
another home directory, which is useful for trying the installer without
changing your own setup. See [work-with-codex details](docs/work-with-codex.md).

The source layout is `skills/flow/` and `skills/underlow/project/`, each with
shared instructions and platform entrypoints. When a platform needs hooks or
other files, add them to its platform directory and the installer will copy
them with its entrypoint.

The profiles are `full`, `medium`, `small`, and `bugfix`. See the
[phase guide](skills/flow/shared/references/phases.md). The detailed
[prompt library](skills/flow/shared/references/prompt-map.md) preserves the
original analysis, planning, implementation, and review criteria. The skill
does not require the former CodeFlow application.

After agreeing on a plan, `flow` proposes a model and reasoning effort for its
developer agents and waits for your choice. It proposes reviewer models and
effort alongside the review plan, once the actual change is known.
