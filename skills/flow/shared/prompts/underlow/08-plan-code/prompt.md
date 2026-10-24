Turn the requirements and design into an ordered implementation plan. The plan
must give the developer enough information to do the work without inventing
product behavior or design decisions.

Use the requirements to decide what the feature must do and what is in scope.
Use the design to decide how the system should be changed. Do not reconsider
decisions already settled in the requirements or design. Revise an earlier
document only when the documents contradict each other or leave out a decision
needed for the plan; do not settle an open product or design question inside
the plan.

Read enough of the repository to find the affected code, existing patterns,
dependencies, and useful validation commands. Do not inspect unrelated areas.

Split the work into tasks when that helps a fresh developer. Order the work so
earlier results provide what later work needs. Make sure every requirement is
covered. When several tasks must use the same data or behavior, explain what
they must agree on. Include the work needed to join the results into the
working feature, the whole-feature checks, and any updates to maintained
documentation once the behavior they describe exists.

Describe what each task must achieve, not every step the developer should take.
Do not prescribe private helpers, algorithms, file organization, exact private
signatures, pseudocode, or detailed test bodies unless the design already decided
them. File paths may show the developer where to start; they are not a complete
list of files that may change.

Use these sections in `plan.md`:
1. A plain-language summary of what the work will deliver.
2. Ordered work and dependencies, with links when separate task files help.
3. Anything that several tasks must agree on.
4. A map from requirements to work and checks for the complete feature.

Put a short reason beside a planning choice when the reason matters. Do not create
separate risk, evidence, decision, or agreement documents. Put optional
task files under `tasks/`.

When separate task files help, write one numbered file per task, in execution
order. Each task contains:
1. Result: what must be true when the task is finished, with the relevant
   requirement IDs.
2. Inputs and dependencies: the documents, current behavior, or earlier task
   results it needs.
3. Work: what it must deliver and how that work joins the rest of the feature.
   Name useful starting places when needed.
4. Behavior to preserve: limits and existing behavior that must not be broken.
5. Verification: what to observe, where to observe it, anything the check needs
   first, and the harmful mistake the check must catch. Do not prescribe the test
   body.

Refer to requirements and acceptance examples instead of copying them. A task must
make sense without conversation history. Expected results must come from the
requirements, not from one possible implementation. Give each task only the
checks needed to show that it produced its result. Put checks that cover several
tasks in `plan.md` instead of repeating them in every task.

Before presenting the plan, check that:
- every required result is assigned to work;
- each task has the inputs it needs before it starts;
- tasks that must agree describe the same data or behavior;
- the tasks join into the complete feature;
- every named check can run and can catch the mistake it names.

On revision, preserve accepted or nonblocking findings for the developer
without changing the plan only because a reviewer assigned a priority label.
Update every affected task and every agreement between tasks, not only the place
named by the reviewer.

When implementation shows the plan is wrong, inspect the work that already
exists. Keep valid completed work. Update work that is obsolete or still
needed so the developer does not repeat finished work.

The plan is ready when it and any tasks can be followed as written and no
required product or design decision is missing. Do not implement code.
