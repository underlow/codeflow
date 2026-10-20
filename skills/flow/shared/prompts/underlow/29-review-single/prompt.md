Independently review the entire change as one agent covering all aspects together.
Do not delegate aspects or launch other agents. For small, use confirmed requirements,
their acceptance cases, and the technical approach in the plan. For bugfix, use the
investigation's expected behavior, reproduction evidence, agreed fix scope, and
regression expectations; no requirements, design, plan, or task files are required.

Identify the full change from the run's recorded Git base through current HEAD and
run-owned working changes. Distinguish unrelated user changes using scope and Git
evidence; state any uncertainty. Never limit review to the latest commit or fix.
Read surrounding callers and consumers needed to understand reachable behavior.

Check these five areas in one report, explaining when an area is irrelevant to
the change:
- Behavior: required results are complete and reachable through every supported
  entry path; logic, state, errors, retries, and component connections work.
- Test quality: tests catch named harmful mistakes and expected results come from
  the contract. For bugs, inspect whether the regression check catches the original
  failure and whether the actual reproduction was rerun after the fix.
- Security: reachable unauthorized actions or sensitive data exposure.
- Performance: material regressions under supported, realistic use.
- Code quality: concrete maintenance problems, unnecessary complexity, or duplication.
For bugs, check that the cause was corrected and nearby behavior remains valid;
a disappearing symptom alone does not establish a fix.

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

Report concrete defects within scope, with a credible trigger and consequence.
High means likely failure in ordinary or required use, or credible data loss,
security breach, or irreversible harm. Medium means material failure in supported
use or a material defect that can escape, with limited or recoverable impact.
Low means a narrow, small, recoverable problem; record it without requiring a fix.
Exclude preferences, hypothetical scale, and unrelated pre-existing problems.
For missing tests or planning details, classify the defect that could escape.
Keep stable finding IDs on repeat reviews. Reassess the complete current input,
not only the last correction. Earlier approval does not excuse a defect.

Inspect validation evidence without running tests, builds, benchmarks, or manual
checks yourself. Missing evidence is not passing validation. Return findings for
correctable high or medium issues, blocked if essential evidence prevents reliable
assessment, or passed when no correctable high or medium defect remains.

Write {{step_output}} with verdict, findings (ID, priority, location, trigger,
consequence, required outcome), and concise coverage conclusions for all aspects.
Mark an irrelevant aspect with a concrete reason. Preserve unavailable checks,
nonblocking findings, and limitations. On passed, include a brief final handoff:
delivered result, validation actually performed, and remaining limitations.
Write only the report and required result files. Do not edit code or planning
documents, commit, or launch agents.
