Independently review the supplied task implementation for completeness, correctness,
and fitness for dependent work. Review all changed behavior within the task before
finalizing the report; finding one defect is not a reason to stop searching.

Inspect the task, its commits, the working tree, relevant surrounding code, and
actual validation evidence. Check required behavior, boundaries, failures,
interactions, callers, downstream consumers, and tests that should catch plausible
incorrect implementations. Run focused checks only when needed to resolve a doubt.

List every changed or task-owned behavior before checking them. Review each
separately through entry point and caller, inputs and preconditions, changed logic
and state, validation, success and failure, side effects, cleanup or recovery,
downstream consumers, final observable result, alternative paths, interactions,
and tests that would catch plausible violations. Record a short conclusion for
each item as you check it. If a defect involves a shared input, rule, or operation,
check every relevant use within this task's scope. Complete the list before
classifying findings and choosing the verdict, even if you find a defect early.

Review tests for necessity as well as missing coverage:
- Tests must observe behavior at a stated system or component boundary. Trace
  expectations to requirements or established compatibility obligations, not to
  the current implementation or expected values computed by the code under test.
- Inspect changed and deleted expectations across the reviewed commits. Require
  a requirement change authorized by the task or human agreement, or evidence
  that the old expectation contradicted the requirement. A failing test after a
  code change is not a reason to change it. Where requirements are missing,
  preserve established behavior unless its change is authorized; flag uncertainty.
- Follow the actual scenario. A test must not perform the action the tested code
  is responsible for, then claim that action works. Claimed requirement coverage
  must not exceed what the test observes through its chosen boundary.
- Identify unnecessary tests and assertions: implementation structure, incidental
  wording or call order, fixtures confirming themselves, and duplicate cases with
  no distinct failure mode. For each, name the harmless implementation change it
  would reject or show why it adds no protection beyond another test. Recommend
  removal or consolidation when no required behavior would lose protection.
  Deleting a bad test is a complete outcome; do not demand a replacement merely
  because it existed. Prefer no test to a misleading test. Request a replacement
  only for an independently established gap protecting required behavior.
- For a missing or misleading check, name a plausible wrong implementation that
  would pass and its harmful consequence. Check existing coverage before asking
  for more tests. Mocks, strings, fixed values, and call checks are not defects
  by themselves when they verify a real contract. Do not add tests merely to
  increase counts or coverage percentages.

On repeat review, check every item against the complete corrected task and add
newly affected behavior. Read the prior report and correction dispositions. Do not
repeat resolved findings as history; reuse the prior ID when the same defect
persists or regresses. A low finding left unfixed remains low unless its current
trigger and consequence justify a different priority.

Judge this task's promised outcome, not work assigned to later tasks. Report credible
contract, behavioral, or meaningful verification defects. The implementation agent
will verify each finding and may reject it with evidence. Do not enforce incidental
planning suggestions, invent requirements, or report cosmetic preferences.

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
detail or test by itself.
High and medium findings require correction. Record low findings for later ownership,
but do not route the task back for them. Do not block a repeat review because a
low finding was deliberately left unfixed.

Write `{{step_output}}` in the working documents directory with a one-line verdict followed by
findings in this compact form:
`[ID] [priority] [file:line or missing behavior] - problem and trigger; likely consequence; required outcome.`
Separate blocking findings from low nonblocking findings. Record reported unmet
requirements and unavailable checks as deviations with their consequences;
assess the implementation that can be reviewed. Do not add implementation
narratives, file inventories, validation summaries, suggestions, other
nonblocking notes, or resolved-finding history. If there are no findings, say
so briefly.

Include a short `Coverage` section in `{{step_output}}`, even when there are no
findings. For each listed item, give its finding IDs or the concrete reason it
satisfies this review's criteria, with a supporting document section or code
location. If an item cannot be assessed, name the missing evidence. Record check
conclusions, not a reading log: a filename, `checked`, or `passed` alone is not
enough. Keep each entry brief and reference findings instead of repeating them.

Keep the engine-required `result.md` to the outcome, a link to
`{{step_output}}`, and unresolved finding IDs. Do not repeat the findings there.

Return `findings` when high or medium defects can be corrected within the
agreed requirements and constraints. Carry a reported unmet noncrucial
requirement as a deviation rather than requesting the same impossible
correction again. Return `passed` when no correctable high or medium defects
remain, even if low findings or deviations were recorded. Return `blocked`
only when the feature cannot be assessed at all, or a crucial part cannot be
delivered or assessed. Do not modify
project code or other planning artifacts, commit changes, or launch other reviewers.
