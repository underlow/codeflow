---
name: architecture-review
description: Inspect architectural friction in a repository or named subsystem and produce a visual HTML report with evidence-backed improvement candidates.
disable-model-invocation: true
---

Run the review with `$ARGUMENTS`. A path or subsystem name narrows the scope;
without one, choose a useful scope from recent changes and explain the choice.
Read [the review instructions](references/architecture-review.md) before acting.
This is a standalone analysis command, not a `flow` phase. Do not implement a
candidate during the review.
