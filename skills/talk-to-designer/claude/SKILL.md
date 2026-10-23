---
name: talk-to-designer
description: Consult a separate Claude designer session when visual design is needed. Offer an existing relevant session or a new one, establish how it should reply, and continue the conversation. Use when asked to talk to Claude Design or a designer.
---

Use `/talk-to-designer` with `$ARGUMENTS` as the design request.
Read [the conversation workflow](references/conversation.md).
Prefer native `ListAgents` and `SendMessage` for discovery and conversation.
Retain the selected peer with the shared script's `connect` command, matching
the selected native peer to its registry entry by project and session identity.
On a later invocation, use `connections --project` to recover that selection
before refreshing the native list. If it cannot be matched, ask rather than guess.
Get this session's current return address from the live tool output or
`CLAUDE_CODE_MESSAGING_SOCKET`. Never reuse a previous caller's address.
If native messaging is unavailable, use the shared script described in the workflow.
When available, `mcp__ccd_session__start_session` can create a separate desktop
Claude Code session with the first-message instructions and task as its prompt.
Use its actual schema and normal user-selected session settings. If unavailable,
ask the user to open a designer session, then discover it again.
