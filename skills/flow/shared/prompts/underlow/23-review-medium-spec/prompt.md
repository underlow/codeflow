Independently review the current combined specification for a medium feature.
Use its purpose and requirements as the behavioral contract and its design as the
technical proposal. Inspect the affected repository code to verify consequential
claims. Check scope, ambiguous behavior, failure and continuation cases, feasibility,
component ownership, shared contracts, and compatibility. Confirm that every material
requirement has a plausible mechanism and that the current version is owner-approved.
Do not require separate concept, requirements, or design documents.

Derive independent acceptance cases from the requirements, not from the proposed
implementation. Give each case an A ID, R IDs, initial state, actions, expected
observations, and important continuations. Missing expected behavior is a finding;
do not invent it. Rebuild affected cases when the specification changes.

Report concrete defects within scope, with a credible trigger and consequence.
High means likely failure in ordinary or required use, or credible data loss,
security breach, or irreversible harm. Medium means material failure in supported
use or a material defect that can escape, with limited or recoverable impact.
Low means a narrow, small, recoverable problem; record it without requiring a fix.
Exclude preferences, hypothetical scale, and unrelated pre-existing problems.
For missing tests or planning details, classify the defect that could escape.
Keep stable finding IDs on repeat reviews. Reassess the complete current input,
not only the last correction. Earlier approval does not excuse a defect.

Write {{step_output}} with a verdict, findings, acceptance cases, and brief coverage
conclusions linking requirements and design decisions to evidence or finding IDs.
Each finding gives an ID, priority, document section, trigger, consequence, and
required outcome. Keep low findings separate. Missing owner agreement is a finding
for the interactive author to resolve, not permission to approve on the user's behalf.
Return findings for high or medium defects or missing agreement, passed when none
remain, or blocked when essential evidence prevents assessment.
Write only the report and required result files. Do not edit the specification,
code, or tests, run checks, create commits, or launch agents.
