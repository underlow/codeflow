Verify and correct the supplied review findings or failed checks.
Work noninteractively.

Use the consolidated findings when the incoming report concerns review findings,
and follow its source references as needed. For a failed-check report, use
the supplied failure evidence. Requirements and acceptance cases govern expected
behavior; the design governs binding decisions; and the plan governs scope,
dependencies, and shared contracts. Follow relevant project instructions.

Inspect current code using the current branch commits, working tree, and relevant prior
reports. Continue valid existing work and preserve unrelated changes.

Verify each claimed defect, its triggering scenario, reachability, impact, and
existing protections before editing.

Assign priority by what can happen if the finding is left unresolved. Consider
both how often the trigger can occur and how much harm follows:
- high: ordinary or required use is likely to fail, or there is a credible risk
  of data loss, a security breach, or another irreversible consequence;
- medium: supported use can fail materially, or a material defect can escape, but
  the trigger or impact is limited or recoverable;
- low: the feature remains shippable; the problem is rare or narrow and its impact
  is small and recoverable.
Do not raise priority for a theoretical worst case without a credible trigger. For
planning and test gaps, classify the defect that could escape, not the missing
detail or test by itself. Correct every confirmed high or medium defect within
scope. Low findings are nonblocking: preserve them for
the final owner, but do not make a separate change solely for them unless the same
change is required by a blocking finding. Reject unsupported findings with evidence.

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

Return fixed when every supplied high or medium finding or failure is corrected,
rejected with evidence, or recorded as a noncrucial deviation that cannot be
corrected under the agreed constraints. Explain each deviation and its
consequence. Report any required correction check that could not run; do not
claim it passed. This means ready for independent re-review, not final acceptance.
No correctable high or medium defect may remain unresolved when returning fixed.

Use this format in {{step_output}}:
1. Every finding ID, verified priority, and disposition: fixed, nonblocking,
   deviation, rejected, needs-replan, or unresolved. Give reasoning for a rejection,
   reprioritization, nonblocking disposition, deviation, or blocker; otherwise
   name the changed location.
2. Checks actually executed and their results.
3. Deviations, unavailable checks, or blocker, when present: the consequence
   and the decision or prerequisite needed.
Do not add a correction narrative, file inventory, or risks section.

Preserve finding identities and prior-round evidence through report references.
In result.md, summarize the outcome and link {{step_output}}.

Commit the completed corrections with a concise message. Do not edit planning
artifacts or original reviews, or launch other agents.
