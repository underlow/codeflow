# work-with-codex

Discuss a task with Codex as a peer. For implementation or review, use
[delegate-to-codex](delegate-to-codex.md).

```sh
./install.sh --with-collab --force
```

Requires Python 3, Codex, and Ghostty (AppleScript with `tty` support), cmux
with its CLI, or agterm with `agtermctl`.

Invoke `/work-with-codex [topic]`. An explicit model/effort is passed to Codex;
otherwise discussion uses its configured defaults. Model aliases live in
`~/.codex/collab/model-aliases.json` and survive installation updates.
An invalid model returns choices before opening a terminal.

The launcher reads the brief from stdin and passes it directly to Codex.
It detects the originating terminal and prints its new terminal's real ID,
a native `SEND` command, and a native `CLOSE` command. Replace `MESSAGE` with
shell-quoted text. Codex receives a native command for replying to Claude.
No session registry, prompt files, logs, send wrappers, or relay processes are used.

- agterm: `session new --no-select`; `session type` with paste framing and Enter.
- cmux: `new-surface --focus false`; `paste --submit` for Codex and `agent message`
  for Claude. Native Claude messaging requires `cmux hooks setup claude`.
  Native messages cannot wake an already-idle Codex.
- Ghostty: AppleScript creation, input with Enter, and close. Ghostty itself may
  activate the app when creating a tab.

Codex executes reply commands with the terminal access its sandbox requires;
the installer does not grant blanket terminal-control permissions.
For Claude-to-Claude communication, use its built-in messaging.

The `.sh` launcher contains Python and is executed directly. Instructions are in
`SKILL.md`; terminal operations are in `scripts/terminals/`, Ghostty's bridge is
`scripts/ghostty.applescript`, and model resolution is `scripts/resolve-model.py`.
