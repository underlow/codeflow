Does the changed logic produce the required result for reachable inputs and event
sequences?

Find incorrect conditions, calculations, ordering, state changes, error handling,
or recovery. Follow a value into its next use when that use determines whether the
result is correct. Do not demand a safeguard without a reachable failure that
needs it.
When the same operation has different modes or separate preview and action steps,
check each one and the state passed between them. If one has a defect, check the
others that use the same logic.

Focus on logic and state within one part. Problems between parts belong to the
integration review.
