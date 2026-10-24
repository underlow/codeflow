Plan the medium feature from its confirmed `specification.md`, which holds the
requirements, binding design, and acceptance examples. Do not invent a
consequential product or design choice; if one is missing or contradictory,
revise the specification first.

Inspect affected code, dependencies, project instructions, and usable checks.
Write `plan.md` with the result, technical approach, shared contracts,
integration, and how requirements and examples will be verified. Divide the work
into tasks by independently verifiable results and dependencies; each task goes
to its own developer, as a section of `plan.md` or a file under `tasks/`. Each
task names its result, inputs, dependencies, behavior to preserve, and checks
with expected observations and the mistake they catch. A single task is right
only for one bounded result. Put whole-feature checks and documentation updates
after the implementation they need. Leave private choices to the developer.

When implementation shows the plan is wrong, keep valid finished work and plan
only what remains.
