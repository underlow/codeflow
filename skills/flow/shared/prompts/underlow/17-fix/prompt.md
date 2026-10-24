Verify and correct the review findings or failed checks selected for a
full-profile change.

Requirements and acceptance examples govern expected behavior; the design
governs binding decisions; the plan governs scope, dependencies, and shared
contracts. Follow each finding's source references as needed. For a failed
check, use the supplied failure evidence. Inspect the current code from the
branch commits and working tree.

When reviewers' recommendations conflict, resolve them against the requirements
and code, and explain how the chosen correction addresses each confirmed
concern.

For ineffective tests, replace missing coverage or remove redundancy without
losing useful coverage. Run checks relevant to the corrections and required by
applicable project or task instructions; do not assume a later review will run
them. Inspect the final diff for incomplete corrections and interactions between
fixes.

Keep the finding IDs you were given so the coordinator can match your
dispositions to the reviews. Do not edit the review findings.
