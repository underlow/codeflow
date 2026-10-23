# CodeFlow skills

Development guidance for Claude Code and Codex. `flow` handles one change from
planning through review. `project` helps form a high-level project goal and stage
plan, then starts or resumes a chosen stage through ordinary `flow`.
Both use shared instructions with small platform entrypoints.
The standalone `architecture-review` command inspects a repository or named
subsystem and writes a visual HTML report of evidence-backed improvement options.

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

This copies `flow`, `project`, `backlog`, `talk-to-designer`, and `architecture-review` to `~/.claude/skills/` and
`~/.agents/skills/`.
Invoke it as `/flow [plan-folder-or-description-file]` in Claude Code or
`$flow [plan-folder-or-description-file]` in Codex. Codex discovers local skills
from `.agents/skills`; `.codex` holds its configuration and rules.

To start or resume a larger project, use `/project [project-file]` in Claude
Code or `$project [project-file]` in Codex. The project skill saves the goal and
stages in `docs/projects/<slug>.md`, without a separate project directory;
reported bugs and technical assumptions remain
unverified. Investigation and implementation belong inside each stage's flow.
After committing the agreed project plan, it offers to start a stage in the
current conversation or gives a command for a new session, for example
`$flow docs/projects/app.md S1` (use `/flow` in Claude Code). No separate
handoff file is needed. Returning to `project` offers to continue an unfinished
flow or start the next eligible stage here. Each flow chooses its own profile
with you and records its outcome, including an agreed conclusion that no change
is warranted. When project confirms all stages are complete, it moves the
project document into `docs/projects/completed/` and updates its links.
Explicitly reopening work moves it back. Existing projects stored in directories
remain supported and are archived with their whole directory.
You can reconsider the overall project plan at any time.

For an architecture audit outside `flow`, run `/architecture-review [path-or-subsystem]`
in Claude Code or `$architecture-review [path-or-subsystem]` in Codex. The command
creates an offline HTML report in a temporary directory and opens it when possible.

`backlog` records explicitly deferred work and confirmed bugs outside the active
task in the repository's `backlog.md` (or its configured backlog). Features retain
their purpose, agreed behavior, boundaries, and completion checks; bugs retain
reproduction evidence, impact, findings, and unknowns. Recording does not start
implementation. Use `/backlog [item-ID or request]` in Claude Code or
`$backlog [item-ID or request]` in Codex; no argument offers open items.

The skill uses ordinary skill discovery and selection. The installer only copies
skill files; it does not modify `AGENTS.md` or `CLAUDE.md`. Automatic selection
depends on the agent and is not a guaranteed session-start hook.

Use `/talk-to-designer [request]` in Claude Code or `$talk-to-designer [request]`
in Codex to consult a separate Claude designer session. It offers relevant open
sessions or a new one and explains how the designer should reply in its first
message. Claude uses native session messaging when available. Codex uses a
Python 3 script to discover local Claude sockets and send messages; the designer
replies through that script into a persistent local inbox. Codex can wait for or
read replies, but they do not automatically wake a finished Codex turn. Saved
connections let a later session resume the conversation. If session creation
is unavailable, the skill asks you to open the designer session yourself.

The separate `work-with-codex` and `delegate-to-codex` skills launch Codex in
Ghostty, cmux, or agterm and use native terminal commands for messages.
Install them explicitly:

```sh
./install.sh --with-collab --force
```

Use `--force` to replace an existing installation. The command above updates an
already installed `flow` while adding `work-with-codex`. `--target DIR` installs into
another home directory, which is useful for trying the installer without
changing your own setup. See [work-with-codex details](docs/work-with-codex.md).

Use `/delegate-to-codex [task]` in Claude Code to assign implementation or review
to Codex in a new tab. Claude briefs Codex, verifies the result, and sends
corrections until the task is complete. If you have not explicitly named a model,
Claude asks before launching. Development permits workspace edits; review runs
read-only. Both skills are included with `--with-collab`. See
[delegation details](docs/delegate-to-codex.md).

The source layout is `skills/flow/`, `skills/underlow/project/`, `skills/underlow/backlog/`, and
`skills/architecture-review/`, each with
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
