# work-with-codex

A Claude Code skill. Claude opens Codex in a new Ghostty tab next to its own,
gives it a brief of the current problem, and the two brainstorm and critique
each other's ideas to find a better solution than either would alone. Both
think independently first, then compare, attack the leading option and
converge. Claude keeps you informed after each exchange, brings the result to
you, and keeps Codex open for the next round; only you end the session. You
can watch the Codex tab and type in either tab.

Invoke with `/work-with-codex [topic]` or by saying "work with codex". Name a
model or effort ("work with codex on gpt-6.1-sol, high effort") and Claude passes
them to `collab.sh start --model <model> --effort <effort>`. Without them Codex
uses `~/.codex/config.toml`. They are set at start; changing the model of a
running Codex would mean driving its `/model` picker, which the skill does not
do.

An explicit model is resolved within that same `start` call. Short names live in
`~/.codex/collab/model-aliases.json`, created once by the installer and preserved
on updates. Exact model IDs and unambiguous display names also work. The launcher
checks the model and explicit effort against the chosen Codex binary's catalog
before creating a session or touching Ghostty; failure returns a model list.
Python 3 is required for this check. Catalog refresh falls back to the bundled
catalog with a warning if unavailable; catalog membership does not prove account
access. No separate model-list exchange is required.

## How the two talk

- **Claude to Codex**: Claude types into the Codex tab through Ghostty's
  AppleScript API (`input text`, then `send key "enter"`). Messages start with
  `[claude]`.
- **Codex to Claude**: Codex runs `~/.codex/collab/collab.sh <id> '<text>'`,
  which writes the message to Claude Code's inbox socket. It arrives in
  Claude's conversation as a message from another session, starting with
  `[codex <id>]`. If Claude is idle, it starts a turn; nobody polls.

Codex runs with `--sandbox read-only`, which blocks sockets. The rule in
`~/.codex/rules/collab.rules` lets exactly `collab.sh` run outside the sandbox
without asking. Codex cannot change what that script does or where it sends:
the script and the session's `target` file live under `~/.codex`, which the
sandbox does not let Codex write.

## Install

```sh
./install.sh --with-collab --force
```

It writes:

| Path | What |
| --- | --- |
| `~/.claude/skills/work-with-codex/` | the skill: `SKILL.md`, `codex-prompt.md`, `scripts/` |
| `~/.codex/collab/collab.sh` | Codex's sender, from `skills/work-with-codex/codex/` |
| `~/.codex/rules/collab.rules` | the rule that pre-approves the sender |

Run it again after changing anything here. Requires Ghostty 1.3+ and `codex`
on `PATH`. `jq` and `nc` ship with macOS.

## Files

| File | Role |
| --- | --- |
| `SKILL.md` | what Claude does: its own homework, the brief, the stages of the discussion, keeping the user in the loop |
| `codex-prompt.md` | Codex's first message: its role as a peer, how to reply; the brief is appended |
| `scripts/collab.sh` | `start`, `send`, `status`, `close` |
| `scripts/ghostty.applescript` | find, open, type into, focus and close Ghostty terminals by id |
| `skills/work-with-codex/codex/collab.sh` | Codex's sender |

A session lives in `~/.codex/collab/<id>/`: `target` (Claude's socket),
`prompt.md`, `launch.sh`, the two terminal ids, and `log.jsonl` with every
message both ways. `close` deletes it.

## Tested on 2026-10-11

Ghostty 1.3.1, codex-cli 0.160.1.

- Codex's sandbox blocks the socket and AppleScript. The rule lets
  `collab.sh` through, in `codex exec` and in the interactive Codex.
- A separate `~/.codex/rules/collab.rules` is loaded; `default.rules` is left
  alone.
- The sandbox cannot write to `~/.codex`, so Codex cannot rewrite the script
  or a session's target.
- A paste followed straight away by Enter submits the message. Two-line and
  80-line messages with quotes, `$` and backticks arrive whole.
- Codex's messages with line breaks, double quotes, `$`, backticks and
  Cyrillic arrive whole.
- `close` quits Codex, closes its tab, and focuses Claude's tab again.
- `start --model gpt-6.1-sol --effort low` reaches Codex as
  `--model gpt-6.1-sol -c model_reasoning_effort="low"`.

Found while testing:

- The rule matches only a plain single-quoted argument. `'\''`, `$'...'`,
  double quotes with escapes and heredocs run inside the sandbox and fail.
  Codex is told to write `’` instead of `'`; the script's error says the same.
- A tab opened through AppleScript gets Ghostty's environment, not the
  shell's, so `launch.sh` carries over `PATH`.
- Ghostty does not report a terminal's tty. `start` finds Claude's tab by
  writing a unique title to Claude's tty and looking it up.

## Open

- A Claude message typed while Codex is still working. Codex's turn-taking
  avoids it; what Codex does with it was not tested.
- A Claude Code session in bypass-permissions mode holds incoming messages
  for the user (codeflow-poc item 2), so Codex's replies would wait. Not tried
  with this skill.
- Only Ghostty is wired up. iTerm2 has a similar AppleScript API; not tried.
