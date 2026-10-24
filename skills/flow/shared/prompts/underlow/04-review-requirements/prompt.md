Review the requirements for fidelity to the user's decisions and for complete
observable behavior. They must say what the product does, not prescribe code.

For each consequential behavior, check entry conditions, expected result,
boundaries, failures, repetition, recovery, later state, and interaction with
other rules. Look for contradictions, examples no rule supports, missing
decisions, and text that materially different products could satisfy. Read code
only to verify a claim about current behavior. Do not invent product decisions.
A repeated leak of implementation detail is one finding.

Derive acceptance examples from what the requirements actually guarantee:
requirement ID, initial state, actions, expected observations, and what happens
next. Report a missing guarantee as a gap instead of guessing. Include the
proposed examples in your response; if you were given examples from an earlier
review, recheck only those the changes affect.
