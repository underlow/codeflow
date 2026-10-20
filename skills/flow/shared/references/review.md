# Independent review

Review the complete change from the run's base commit through current HEAD and
run-owned working changes. Read surrounding callers and consumers where needed.
Separate unrelated user changes. Check the behavior against the agreed contract,
including changed or deleted test expectations. Do not treat a passing test or a
reviewer's confidence as proof of the user-visible result.

Before the first code review, the coordinator proposes a concrete review plan to
the user: what changed, which risks deserve an independent reviewer, which can
be covered together, and why. Wait for the user's selection or agreement before
launching reviewers. Consider implementation completeness, correctness and
reliability, integration, test quality, security, performance, and code quality.
These are questions to assess, not seven mandatory agents or seven reports. For a
narrow change one whole-change reviewer may suffice. Use specialists when the
risk or code boundary benefits from independent attention. Respect available
agent concurrency; do not start redundant reviewers merely to fill slots.

Before recording findings, a reviewer identifies the changed user actions and
code operations in its scope. Check each through entry points, inputs, state
changes, failure and retry paths, downstream consumers, and observable results.
When a defect uses a shared mechanism, inspect other reachable uses before
reporting its extent. Finish the assigned scope even after an early defect. On
re-review, include newly affected behavior and prior findings.

A finding needs a reachable trigger, location or missing behavior, likely
consequence, and required outcome. Classify urgency from those facts, not from a
hypothetical worst case or a reviewer's preferred design. High and medium
findings normally require correction; low findings are nonblocking. Inspect
whether a test catches a plausible harmful mistake using expected behavior
established independently of the implementation. A test that performs the
product's action itself or only confirms its fixture does not prove that action.
For changed or deleted expectations, require an agreed behavior change or
evidence that the old expectation was wrong. Remove or revise misleading tests
when needed; more tests are not an end in themselves. Reviewers do not edit code
or commit.

The coordinator groups duplicate findings and preserves source references. No
separate consolidation agent or file is required. Give the fixer the original
findings and contract. The fixer checks reachability, severity, protections, and
all affected uses before changing code; it may reject a finding with evidence.
It resolves confirmed defects and runs relevant checks. If a reviewer calls a
problem high but the user considers even its demonstrated consequence
acceptable, present the exact scenario, impact, and both assessments to the
user. Record the user's disposition and its consequence. Do not keep sending the
same accepted risk back through review unless new evidence changes it.

After a fix, select fresh independent review based on the corrected paths,
previous findings, and newly affected interfaces. A targeted reviewer still
checks the complete current behavior of its assigned scope, not just the last
diff. Rerun a broader review when a correction changes shared behavior or
invalidates earlier coverage. A test-only change may affect behavioral
expectations; a local code change may affect integration or performance. Explain
the actual impact rather than using file type alone to skip or launch a reviewer.
If a new broad round seems useful after corrections, discuss its expected value
with the user. Repeated findings or substantive disagreement require a decision,
not an automatic loop. Carry unresolved or user-accepted findings into delivery.
