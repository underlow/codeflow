Does the delivered change produce the agreed behavior through every supported
way to use it?

For each affected requirement and acceptance case, find the code users actually
reach. Check behavior that must stay the same or must not be added. Placeholders,
examples, and unused code do not deliver a requirement. Trace each supported
entry path through calls, data, configuration, and state changes to the result
the user sees. Check that no path still follows the old behavior or bypasses the
change.

Look for incorrect conditions, calculations, ordering, validation, error
handling, and recovery. Check what happens on cancellation, a later attempt, or
a different mode such as preview versus action. Follow values into their next
use when that use determines the result. Across components, check registration,
wiring, compatible values and errors, ownership, and state lifetime. If a defect
involves shared logic or input, inspect its other reachable uses.

Report missing, incorrect, or unintended behavior with a concrete trigger and
consequence. Do not demand a safeguard without a reachable failure or report an
unrelated change only because it is outside the plan. Report a credible defect
you encounter even if another focus guide would normally cover it.
