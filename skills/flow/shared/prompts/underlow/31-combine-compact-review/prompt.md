Combine all seven aspect reports from the current medium-feature review round.
Confirm that each expected aspect has a complete current report. Never substitute
an earlier passing report. Return blocked if a report is missing, stale, or unusable.
Preserve every finding, priority, source ID, location, trigger, consequence, and
required outcome. Merge only findings describing the same defect and trigger;
keep their source IDs. Retain the higher priority on disagreement for the fixer
to assess. Do not verify, reject, reclassify, or repair findings yourself.

Write {{step_output}} with the verdict and consolidated findings, separating low
findings from high and medium ones. Refer to source coverage instead of copying
it. Preserve deviations and unavailable checks. Return findings if any current
report has high or medium findings, otherwise passed. On passed, include a brief
final handoff using implementation evidence: delivered result, checks actually
performed, and remaining limitations. Never treat an unexecuted check or placeholder as passing validation.
Write only the report and required result files. Do not edit code, contracts,
plans, or original reports, run checks, create commits, or launch agents.
