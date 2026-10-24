Does the change let someone perform an unauthorized action or expose sensitive
data?

Report only reachable problems. State who can trigger the behavior, how their input
reaches it, and which protection is missing. Check permission where the action is
performed; a restriction in the interface alone is not enough.
For each command, file change, or release of sensitive data affected by the
change, trace the input it uses. If one action can use an input to affect the
wrong data, inspect other actions that use that input.

Do not expose secrets or attack live systems.
