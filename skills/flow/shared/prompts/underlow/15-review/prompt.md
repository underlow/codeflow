Establish what changed before reviewing it. For a Git run, read the base commit
from the plan's progress.json. Review all commits from that commit to the current
HEAD, plus uncommitted changes made during this run. Distinguish flow changes
from unrelated user changes using the task scope and Git evidence. If ownership
is unclear, state that limitation rather than including unrelated work. Do not review only
the latest commit or the latest fix. Read the surrounding code needed to
understand each changed path, not only the diff.

If the run has no recorded Git base commit, state how you identified the change
and what you could not establish.

Review the complete development change for the assigned aspect. Start by listing
the affected user actions and code operations relevant to this aspect, using the
requirements, acceptance cases, design, and code. Review each separately: how it
starts, what it checks and changes, what happens on failure or retry, and what state
it leaves. Follow the behavior into existing code where needed. Record a short
conclusion for each item as you check it.

When you find a defect, check every listed operation where the same input, rule,
or mechanism could cause it, including relevant code that was not edited. Record
the conclusion for each operation; do not assume other uses are safe. Report every
affected place. Use one finding when the cause and required correction are the
same; otherwise use separate findings. Complete the list before classifying
findings and choosing the verdict, even if you find a defect early. On repeat
review, check prior findings and the complete current change again, not just the
fixer's edits. Update the coverage conclusions for the current change.

Requirements and acceptance cases define behavior and scope; binding design
decisions define technical constraints. Report a contradiction or missing decision
only when it prevents a reliable review. Earlier approval does not excuse a defect.

Keep findings within the change's scope. Report credible actionable defects for
this aspect, including serious defects that overlap another aspect. The fixer will
verify each finding and may reject it with evidence. Exclude preferences,
speculative optimization, and unrelated pre-existing problems. Do not run tests,
builds, benchmarks, scanners, or manual checks.

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
High and medium findings require correction. Record low findings for the final owner,
but do not invoke the fixer for them. On repeat review, keep the prior ID for a
low finding that still exists; do not block because it was deliberately left
unfixed. Reassess its priority if its current trigger or consequence changed.

Write the assigned report to `{{step_output}}` in the working documents directory
with a one-line verdict followed by findings in this
compact form:
`[aspect-ID] [priority] [file:line or missing behavior] - problem and trigger; likely consequence; required outcome.`
Separate blocking findings from low nonblocking findings. Record reported unmet
requirements and unavailable checks as deviations with their consequences;
assess the change that can be reviewed. Do not add file inventories,
implementation narratives, validation summaries, suggestions, other
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

Use `findings` when high or medium defects can be corrected within the agreed
requirements and constraints. Carry a reported unmet noncrucial requirement
as a deviation rather than requesting the same impossible correction again.
Use `passed` when no correctable high or medium defects remain, even if low
findings or deviations were recorded. Use `blocked` only when the feature
cannot be assessed at all, or a crucial part cannot be delivered or assessed.
Write only `{{step_output}}` and required result files. Do not edit code, tests, other planning documents, or
Git state, ask questions, or launch agents or workflows.
