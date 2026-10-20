Review every task and the full current plan before implementation. For medium,
use requirements and design in the combined specification and acceptance cases in
its independent review. For small, use confirmed requirements and their acceptance
cases; the technical approach is in the plan. Do not demand absent upstream stages.

Check requirement coverage, independent expected outcomes, task order and inputs,
shared contracts, actual repository integration points, important failures and
continuations, and executable verification. The final task must cover integration,
required whole-feature checks, and necessary documentation updates. There is no
per-task review to catch gaps before dependent tasks run. Verify technical claims
against code. For small, check that consequential technical choices have agreement
or explicit delegation; ordinary local details do not require extra approval.

Report concrete defects within scope, with a credible trigger and consequence.
High means likely failure in ordinary or required use, or credible data loss,
security breach, or irreversible harm. Medium means material failure in supported
use or a material defect that can escape, with limited or recoverable impact.
Low means a narrow, small, recoverable problem; record it without requiring a fix.
Exclude preferences, hypothetical scale, and unrelated pre-existing problems.
For missing tests or planning details, classify the defect that could escape.
Keep stable finding IDs on repeat reviews. Reassess the complete current input,
not only the last correction. Earlier approval does not excuse a defect.

Write {{step_output}} with a verdict, findings, and brief coverage conclusions for
required results, dependencies, shared contracts, and whole-feature checks. Each
finding gives ID, priority, task or requirement, trigger, consequence, and required
outcome. Return findings for high or medium defects or missing required agreement,
passed when none remain, or blocked when essential evidence prevents assessment.
Do not edit the plan or contract, implement code, run checks, commit, or launch agents.
