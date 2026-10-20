Verify and correct the supplied whole-feature findings noninteractively. The
coordinator may supply findings from one or several selected reviewers.

For medium, the combined specification owns requirements and binding design, its
independent review provides acceptance cases, and the plan owns task dependencies.
For small, the requirements include acceptance cases and the plan includes the
technical approach. Use those current documents; do not require separate upstream
documents or invent additional product decisions. Follow applicable project instructions.

Report concrete defects within scope, with a credible trigger and consequence.
High means likely failure in ordinary or required use, or credible data loss,
security breach, or irreversible harm. Medium means material failure in supported
use or a material defect that can escape, with limited or recoverable impact.
Low means a narrow, small, recoverable problem; record it without requiring a fix.
Exclude preferences, hypothetical scale, and unrelated pre-existing problems.
For missing tests or planning details, classify the defect that could escape.
Keep stable finding IDs on repeat reviews. Reassess the complete current input,
not only the last correction. Earlier approval does not excuse a defect.

Verify each finding's trigger, reachability, impact, and existing protections.
Correct supported high and medium defects and affected nearby paths. Reject
unsupported findings with evidence; preserve low findings without separate work
solely for them. Preserve valid implementation and unrelated user changes.
Add or repair meaningful behavior tests where needed, run affected checks and
required whole-feature validation, and update maintained documentation affected
by the corrections. Do not weaken expected results to make checks pass.
Return revise-plan if correction needs different task scope, binding technical
decisions, or requirements; state the conflict so planning can route it upstream.
Return blocked for unavailable crucial prerequisites. Return fixed only after all
correctable high and medium findings are resolved or rejected with evidence.

Write {{step_output}} with each finding ID and disposition, actual validation
results, and limitations. Explain rejections and changed priorities. Commit the
corrections. Do not edit the plan, specification, or original reviews, or launch
agents. The coordinator selects independent re-review for the affected behavior
and interfaces.
