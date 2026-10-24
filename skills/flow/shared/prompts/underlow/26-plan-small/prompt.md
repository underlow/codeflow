Plan the small feature from its confirmed requirements and acceptance examples.
Include the needed technical approach in the plan; there is no separate design
document. Inspect affected code, project instructions, and usable checks. Decide
routine local engineering details from existing patterns.

Discuss consequential choices about shared contracts, compatibility, ownership,
or lifecycle with the user unless already delegated. Explain the mechanism and
meaningful alternatives, then wait for an actual answer. A choice changing
observable behavior belongs in the requirements; revise them first.

Write one plan that states the result, approach, work order, integration, and
verification. Create task files only if separate bounded tasks help a fresh
developer. Tasks may be numbered sections of plan.md; each is a separate
assignment for a fresh developer. Choose boundaries by verifiable results and
dependencies, not file layout. Each task needs its inputs, behavior to
preserve, expected result, and checks that would catch a plausible harmful
mistake. A one-task plan must be executable without the planning chat. Leave
private helpers, exact signatures, and test bodies to the developer.

Place required whole-feature checks and documentation work after the relevant
implementation. Do not claim planned checks ran. When implementation shows the
plan is wrong, keep valid completed work. Do not implement code.
