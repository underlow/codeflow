Verify and correct the supplied review findings or failed checks.
Work noninteractively.

Use the findings selected for correction, and follow their source references
as needed. For a failed check, use
the supplied failure evidence. Requirements and acceptance cases govern expected
behavior; the design governs binding decisions; and the plan governs scope,
dependencies, and shared contracts. Follow relevant project instructions.

Inspect current code using the current branch commits, working tree, and relevant prior
reports. Continue valid existing work and preserve unrelated changes.

Verify each claimed defect, its triggering scenario, reachability, impact, and
existing protections before editing.

Explain any difference between a reviewer's claimed impact and what the code
shows. A priority label alone does not authorize a change. Correct verified
findings selected by the coordinator and user. Preserve accepted or nonblocking
findings for delivery without a separate change solely for them. Reject
unsupported findings with evidence. Bring a consequential disagreement back to
the coordinator rather than silently downgrading or fixing it.

Fix the underlying failure, including affected callers and nearby behavior,
rather than only the reported example. Resolve conflicting recommendations
against requirements and code; explain how the chosen correction addresses
each confirmed concern. Reviewer suggestions do not bind implementation
details. For every correction, identify affected requirements, acceptance cases,
entry paths, callers, consumers, failure paths, and tests. Re-evaluate all retained
relevant cases against the complete corrected change, including interactions between
corrections. Resolve defects exposed by a correction instead of leaving them for the
next review. Keep changes limited to corrections and necessary supporting work.

Add or update meaningful behavioral tests where needed, deriving expected
results from requirements and acceptance cases. For ineffective tests,
replace missing coverage or remove redundancy without losing useful coverage.
Do not weaken expectations to obtain passing results.

Run checks relevant to the corrections and required by applicable project
or task instructions. Record actual results and unavailable checks.
Inspect the final diff for incomplete corrections and interactions between
fixes. Do not assume later steps will perform validation.

Return fail if a correction crucial to the main user journey or safe use
requires changing agreed requirements, binding design, shared contracts, or
planned task scope or dependencies. Explain
the conflict, evidence, decision needed, affected work, and partial changes.
A fixable implementation defect is not a reason to replan.

Return blocked only when the requested feature cannot be implemented at all, or
a missing part is crucial: without it, the feature's main user journey cannot
work or cannot be used safely. Record unavailable checks and noncrucial
deviations with their consequences for the final handoff.

Return fixed when every selected finding or failure is corrected or rejected
with evidence, and remaining decisions or deviations have been reported to the
coordinator. Explain their consequences. Report any required check that could
not run; do not claim it passed. This means ready for independent re-review,
not final acceptance.

Use this format in the final response:
1. Every selected finding ID and disposition: fixed, accepted risk,
   nonblocking, deviation, rejected, needs-replan, or unresolved. Give reasoning
   for a rejection, changed impact assessment, deviation, or blocker; otherwise
   name the changed location.
2. Checks actually executed and their results.
3. Deviations, unavailable checks, or blocker, when present: the consequence
   and the decision or prerequisite needed.
Do not add a correction narrative, file inventory, or risks section.

Preserve finding identities and prior-round evidence through the supplied finding
references.

Commit the completed corrections with a concise message. Do not edit planning
artifacts or original reviews, or launch other agents.
