Would the tests detect concrete violations of the required behavior, and can their
results be trusted?

Review tests for necessity as well as missing coverage:
- Tests must observe behavior at a stated system or component boundary. Trace
  expectations to requirements or established compatibility obligations, not to
  the current implementation or expected values computed by the code under test.
- Inspect changed and deleted expectations across the reviewed commits. Require
  a requirement change authorized by the task or human agreement, or evidence
  that the old expectation contradicted the requirement. A failing test after a
  code change is not a reason to change it. Where requirements are missing,
  preserve established behavior unless its change is authorized; flag uncertainty.
- Follow the actual scenario. A test must not perform the action the tested code
  is responsible for, then claim that action works. Claimed requirement coverage
  must not exceed what the test observes through its chosen boundary.
- Identify unnecessary tests and assertions: implementation structure, incidental
  wording or call order, fixtures confirming themselves, and duplicate cases with
  no distinct failure mode. For each, name the harmless implementation change it
  would reject or show why it adds no protection beyond another test. Recommend
  removal or consolidation when no required behavior would lose protection.
  Deleting a bad test is a complete outcome; do not demand a replacement merely
  because it existed. Prefer no test to a misleading test. Request a replacement
  only for an independently established gap protecting required behavior.
- For a missing or misleading check, name a plausible wrong implementation that
  would pass and its harmful consequence. Check existing coverage before asking
  for more tests. Mocks, strings, fixed values, and call checks are not defects
  by themselves when they verify a real contract. Do not add tests merely to
  increase counts or coverage percentages.
