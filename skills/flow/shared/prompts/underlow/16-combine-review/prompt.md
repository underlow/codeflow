Consolidate the seven current aspect reports into `{{step_output}}` for the
fixer. Work noninteractively.

Confirm that every aspect report belongs to the current round. Preserve every
finding. Merge findings only when they describe the same defect and trigger; keep
the source IDs, priority, location, problem, consequence, and required outcome. Do
not verify, reject, expand, repair, or reclassify findings. When priorities differ,
retain the higher priority and mark the disagreement for the fixer to reassess.

Coverage entries describe the checks performed, not additional findings. Leave
them in the source reports; do not copy them into the consolidated findings.

Write findings in this compact form:
`[consolidated ID] [priority] [source IDs] [location] - problem and trigger; likely consequence; required outcome.`
Separate high and medium blocking findings from low nonblocking findings. Preserve
low findings even when their source aspect passed. If every report passed with no
findings, say so briefly. Preserve reported deviations and unavailable checks
with their consequences for the final handoff. Do not add summaries, coverage
tables, evidence narratives,
recommendations, or prior-round history.

Return `findings` when the current reports contain high or medium findings, `passed`
when they contain none even if low findings were recorded, or `blocked` when a
required current report is missing or unusable. Write only
`{{step_output}}` and required result files. Do not edit code, planning
documents, original reviews, or Git state, run checks, or ask questions.
