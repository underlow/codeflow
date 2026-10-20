Do the changed parts work together to deliver the required behavior?

For each required behavior that uses more than one part of the application,
start at every supported way a user can reach it. Follow the data and calls
through those parts to the result the user sees. Check whether another
supported way still follows the old behavior or handles an error differently.

Find missing registration or wiring, configuration that does not reach the code
that needs it, incompatible values or errors passed between parts, and supported
ways of using the feature that bypass the change. Check ordering and lifetime
across boundaries when they affect the result.

Focus on problems between parts. Problems within one part belong to the
correctness review.
