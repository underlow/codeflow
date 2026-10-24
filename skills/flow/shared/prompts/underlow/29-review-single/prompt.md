Review the complete change as one agent. For a medium feature, use the
confirmed specification and plan. For a small feature, use the confirmed
requirements, acceptance examples, and technical approach. For a bugfix, use the
agreed expected behavior, original failure or reproduction, fix scope, and nearby
regression expectations. Do not require feature-planning documents for a bugfix.

Inspect all changes of this flow, including uncommitted work. Follow supported
entry paths, surrounding callers and consumers, failures, retries, and later actions. For a
bugfix, check that the cause was corrected and nearby behavior still works; a
disappearing symptom alone is insufficient. Check the original reproduction
after the fix when it can be done safely, or state why it was unavailable.

Cover the risks named in your assignment, using the supplied aspect files. For changed tests, check that expectations come from
the contract or established compatibility and that the test would catch a
plausible wrong implementation. Changed or deleted expectations need an agreed
behavior change or evidence that the old expectation was wrong. Unnecessary or
misleading tests are findings only when they have a concrete cost or let a
material defect escape.
