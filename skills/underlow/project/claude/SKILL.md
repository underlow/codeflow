---
name: project
description: Research a large project, maintain its evolving stage roadmap, and hand a chosen stage to a separate flow session. Does not choose flow profiles or run development stages.
---

Use this skill as `underlow/project`. Run it with `$ARGUMENTS`. With no argument,
find existing projects in the current repository or start a new one. A path
argument selects a project document or a stage handoff.

Use Claude's native Agent tool for bounded research when independent work would
materially help. The user chooses the next stage; hand it to a separate
ordinary `/flow` session rather than running flow inside this skill.

Read [the project workflow](references/project.md) before acting.
