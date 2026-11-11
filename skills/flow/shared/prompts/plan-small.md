Plan the small feature from its confirmed `problem.md`. There is no separate
requirements or design document: the plan carries the requirements and the
technical approach. Inspect affected code, project instructions, and usable
checks, and decide routine details from existing patterns.

Discuss consequential choices about shared contracts, compatibility, ownership,
or lifecycle with the user unless delegated: explain the mechanism and
alternatives, and wait for an answer. Settle consequential behavior here so
developers do not invent it.

Write `plan.md` with:

1. Requirements: R IDs, observable behavior, relevant failures and boundaries,
   compatibility, and behavior to preserve.
2. Acceptance examples: A ID, R IDs, initial state, action, and expected result.
3. The result, approach, work order, integration, and verification.
4. Tasks, drawn by verifiable results and dependencies, not files. Each task
   goes to its own developer and names its inputs, behavior to preserve,
   expected result, and checks that would catch a plausible harmful mistake.
   Put whole-feature checks and documentation after the implementation they
   need. Leave helpers, signatures, and test bodies to the developer.

Use this as the default structure; merge or omit unneeded sections, add missing
ones, and vary order and detail to suit the plan and its tasks. Do not write
filler to satisfy the template or omit important context because it has no
section. State shared context once. Tasks must preserve the agreed technical
approach without predesigning local implementation details.

Name the automated tests each task adds: the behavior, the boundary it is
observed at, and the mistake it catches. Other checks are run once and
reported. Follow [tests.md](../references/tests.md). Record changes needing
approval as described in [approval.md](../references/approval.md).

When implementation shows the plan is wrong, keep valid finished work and plan
only what remains.
