# delegate-to-codex

Delegate implementation or review to Codex; inspect the result and send
corrections until accepted. Installed with `./install.sh --with-collab --force`.

Invoke `/delegate-to-codex [task]`. Claude asks which model to use unless the user
already named it. `develop` permits workspace edits; `review` is read-only.
Changing review to implementation requires user authorization and a new launch.

The launcher returns Codex's real terminal ID and native send/close commands.
Claude verifies changes or review evidence, sends corrections when needed, and
closes the worker after accepting the result unless asked to keep it open.
Blockers leave the task open.

Both skills share the [terminal launcher](work-with-codex.md). Their instructions
and worker prompts differ; edit the shared scripts only in `work-with-codex`.
