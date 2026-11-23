---
name: flow
description: Plan, develop, and review a change with phase guidance, fresh agents, and resumable work across Git worktrees.
---

Run the flow with `$ARGUMENTS`. An empty argument means offer unfinished plans or
start a new flow. A new flow starts with the problem step; choose the profile
only after it.

Use Claude's native Agent tool for fresh implementation and independent review
agents, or Codex through `delegate-to-codex` when the chosen model preset is
`codex`. Give each agent the exact checkout, relevant contract, task, and file
boundaries.

Start with [the coordinator instructions](references/coordinator.md) and
[the phase guide](references/phases.md). Consult the relevant section of
[workspace and resume rules](references/execution.md) when resolving a request,
managing the checkout or state, resuming, or delivering. Read the
[review guide](references/review.md) before assigning a reviewer.
