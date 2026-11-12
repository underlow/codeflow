Does the change make the code harder to understand, verify, or extend than its
required behavior demands?

Independently derive a simple solution from the task and requirements, then
compare it with the implementation. Check existing code, libraries, and platform
APIs. Added complexity needs a required benefit or a demonstrated limitation of
the simpler option; passing tests alone do not justify it. Verify an alternative
meets the same requirements with comparable reliability before calling its
absence a defect; otherwise state what needs investigation.

Look for tangled responsibilities, duplicated rules, hidden coupling, unclear
state ownership, misleading abstractions, dead code, and difficult control flow.
Show the concrete maintenance consequence: for example, a supported behavior
change must be made in several places that can diverge, or a reader cannot tell
which component owns a state transition. Inspect actual callers before claiming
code is unnecessary or dead.

Do not turn style preferences into defects or request a broad refactor unrelated
to this change. Validation, failure handling, compatibility, and security
controls are not needless complexity merely because they add code.
