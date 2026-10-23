# delegate-to-codex

A Claude Code skill that delegates implementation or review to Codex in a new
Ghostty tab. Claude owns the brief, inspects the result, and sends corrections;
Codex does the assigned work. Requires the same Ghostty/macOS environment and
Claude inbox socket as [work-with-codex](work-with-codex.md).

```sh
./install.sh --with-collab --force
```

This installs both Claude skills and the shared Codex sender and approval rule.
The installer copies the existing `work-with-codex/claude/scripts/` transport
into each installed skill. The delegation skill supplies its own worker prompt.
Edit the transport once in `work-with-codex`; reinstall to update both skills.

Invoke `/delegate-to-codex [task]`, or ask Claude to hand development or review
to Codex. Name the model in the request, or Claude must ask which model to use
and wait for the answer. The transport also rejects delegation without an
explicit `--model`. Effort follows configuration unless explicitly specified.

The launcher accepts `start --task develop|review --model <model>`:

- `develop` uses `--sandbox workspace-write --ask-for-approval on-request`.
- `review` uses `--sandbox read-only --ask-for-approval on-request`.

The existing `work-with-codex` launch remains a read-only peer discussion and
retains its configured model default. The `delegate-to-codex` installation
defaults to the development task if the task flag is omitted, and still requires
an explicit model. Specify the mode in both the launch and brief. Changing a
review into development requires authorization and a new development session.

Both skills use the same `send`, `status`, and `close` commands, session storage,
and asynchronous replies prefixed `[codex <id>]`. Claude must inspect actual
changes or findings before accepting a completion report. Sessions stay open
for follow-up until the user asks to close them.

Installing the sender approval rule permits sending replies to Claude; it does
not grant unrestricted file changes, network access, or deployment permissions.
