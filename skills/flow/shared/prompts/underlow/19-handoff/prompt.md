Write {{step_output}} for the product owner: what was delivered against the
agreed requirements, what was verified, and what remains unresolved.
Use plain language; keep technical detail in linked evidence.

Use relevant recorded decisions and final implementation, validation, review, and documentation evidence.
Base claims on evidence applicable to the final implementation;
do not treat an earlier passing check or a completion claim as proof.

Use this concise format in {{step_output}}:
1. Delivered outcome: what users can now do, against the agreed requirements.
2. Verification: what checks and reviews actually established, with links to
   evidence applicable to the final implementation. Do not imply planned checks ran.
3. Unmet requirements or essential verification gaps, only when present: material
   deviations or limitations, failed or missing checks, product consequences, and
   remaining work or acceptance needed. Recording an issue does not resolve it.
4. Documentation: relevant links, or why no update was needed.
Keep technical detail in linked evidence; do not reproduce task reports, add a
routine risks section, or create another authored handoff document.
Returning done means the handoff report is complete, not that the product is ready.

Lead with what users can now do. Distinguish implemented behavior,
verified behavior, and recorded user acceptance. State readiness only
to the extent supported by evidence.

Carry forward unresolved deviations from the documentation report
prominently; do not imply they were approved or cleared. A known
failure, deviation, or verification gap belongs in the summary.
If missing or contradictory evidence prevents a reliable account,
report the precise blocker.

Summarize existing evidence; do not perform another implementation
review, rerun checks, or make product decisions.
Write only {{step_output}} and the engine-required result files.
Keep result.md to a short transport note: state the selected outcome and link
to {{step_output}}. Do not repeat the summary there.
