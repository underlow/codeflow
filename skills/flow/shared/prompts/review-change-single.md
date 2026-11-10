Review the complete change alone, covering the risks named in your assignment
with the supplied aspect files. The contract is what your assignment names: `problem.md`
with a specification and plan, with a plan that carries requirements and the
technical approach, or alone for a bug fix.

Check whether the implementation reveals a problem with the approach itself,
including local fixes that leave a shared architectural cause intact. Conformance
to the design does not rule out a finding about the approach.

Follow entry points, surrounding callers and consumers, failures, and later
actions. For a bug fix, check that the cause is corrected and nearby behavior
still works; a vanished symptom is not enough. Rerun the original reproduction
when it is safe, or say why not.

For changed tests, check that expectations come from the contract or established
compatibility and would catch a plausible wrong implementation. A changed or
deleted expectation needs an agreed behavior change or evidence that the old one
was wrong. Report tests that [tests.md](../references/tests.md) excludes, and
other unnecessary or misleading tests only when they have a concrete cost or let
a defect through.
