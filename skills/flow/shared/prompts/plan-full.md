Turn the requirements and design into an ordered implementation plan that lets a
developer work without inventing product behavior or design decisions. Do not
reopen settled decisions; if the documents contradict each other or miss a
decision the plan needs, revise them first.

Read enough of the repository to find affected code, patterns, dependencies, and
usable checks.

Split the work into tasks when that helps a developer, ordered so each task has
what it needs. Cover every requirement. Where tasks must use the same data or
behavior, state what they agree on. Include integration work, whole-feature
checks, and documentation updates after the behavior they need exists. Describe
what each task must achieve, not how; file paths are starting points, not a
complete list. Do not prescribe pseudocode, private helpers, or test bodies
unless the design decided them.

Sections of `plan.md`:

1. What the work will deliver, in plain language.
2. Ordered tasks and dependencies, with links when tasks are separate files.
3. What tasks must agree on.
4. A map from requirements to tasks and whole-feature checks.

Each task, as a section or a file under `tasks/`:

1. Result: what must be true afterwards, with requirement IDs.
2. Inputs: documents, current behavior, or earlier results it needs.
3. Work: what it delivers and how it joins the rest.
4. Behavior to preserve.
5. Verification: what to observe and where, setup it needs, and the harmful
   mistake it catches.

A task must make sense to a developer who has only the documents. Refer to
requirements instead of copying them, and take expected results from the
requirements, not from one possible implementation. Checks spanning several
tasks go in `plan.md`.

Before presenting, check that every result is assigned, every task has its
inputs, agreeing tasks describe the same thing, the tasks add up to the feature,
and every check can run and would catch its mistake. On revision, update every
affected task and agreement, not just the place a reviewer named. When
implementation shows the plan is wrong, keep valid finished work and plan only
what remains.
