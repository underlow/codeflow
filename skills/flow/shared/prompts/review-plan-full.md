Review whether the plan can deliver the agreed behavior without a developer
inventing a product or design decision. Each task will go to a separate
developer who has only the documents. Flag a task over two days of work for a
developer who knows the code, and say how to split it.

Start from the original request, agreed behavior and acceptance examples.
Work out who needs which results and when. Then examine the proposed design:
if you remove a responsibility it introduces, which agreed scenario or existing
constraint would fail? Trace dependencies between proposed mechanisms back to
that need. Recommend removing work whose only justification is another
unnecessary mechanism.

For the work that remains, consider both questions independently:
- Does the existing code offer a simpler way to deliver the same behavior?
  Explain which work would disappear and why the agreed guarantees still hold.
- Could relaxing or dropping one requirement eliminate substantial work while
  preserving the main goal? Give the affected user scenario, what the user could
  still do, what they would lose, and which mechanism would disappear.

Report concrete opportunities you find. Either question may yield none.

Consider the tasks together. What will the system look like once they are
complete? Will it preserve the component boundaries and responsibilities set
out in the design? If you find a mismatch, identify the tasks that lead to it
and explain why it matters.
Check that every required result is assigned, dependencies arrive before they
are needed, tasks agree on shared data and behavior, and the results join
through the application's real entry points, including failures, recovery, and
compatibility. Each named check must be executable, state an expected
observation from the requirements, and catch a plausible harmful mistake. Verify
claims about the existing code. When a gap affects shared work, check every
dependent task.

Report contradictions and missing decisions, not private details the developer
can choose. Do not ask for pseudocode, helper structure, copied requirements, or
test bodies.

Flag planned automated tests that [tests.md](../references/tests.md)
excludes, and changes from [approval.md](../references/approval.md) that are
not recorded as approved.
