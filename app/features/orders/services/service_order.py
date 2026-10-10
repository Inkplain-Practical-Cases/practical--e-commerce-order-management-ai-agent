"""Domain service: deterministic STEP-1 acknowledgement.
ICS layer: service
CRD component: be.service_order
Called by: handle_order
Calls: none
Why: provides an independently testable functional slice.
Without: no business response to inspect.
Step: added in STEP-1.
"""
def service_order(value: str) -> str:
    """Return a safe deterministic acknowledgement of the input."""
    # Processing is deliberately limited: later steps add integrations.
    return "Validate the order request before any payment or inventory mutation; input length: " + str(len(value.strip()))
