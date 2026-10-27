Plan the small feature from its confirmed `requirements.md`. The plan also
carries the technical approach, since there is no design document. Inspect
affected code, project instructions, and usable checks, and decide routine
details from existing patterns.

Discuss consequential choices about shared contracts, compatibility, ownership,
or lifecycle with the user unless delegated: explain the mechanism and
alternatives, and wait for an answer. A choice that changes behavior goes to the
requirements first.

Write `plan.md` with the result, approach, work order, integration, and
verification. Draw tasks by verifiable results and dependencies, not files; each
task goes to its own developer and names its inputs, behavior to preserve,
expected result, and checks that would catch a plausible harmful mistake. Put
whole-feature checks and documentation after the implementation they need. Leave
helpers, signatures, and test bodies to the developer.

Name the automated tests each task adds: the behavior, the boundary it is
observed at, and the mistake it catches. Other checks are run once and
reported. Follow [tests.md](../references/tests.md). Record changes needing
approval as described in [approval.md](../references/approval.md).

When implementation shows the plan is wrong, keep valid finished work and plan
only what remains.
