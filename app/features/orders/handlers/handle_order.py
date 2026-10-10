"""Handler: forward validated input to domain service.
ICS layer: handler
CRD component: be.handle_order
Called by: receive_order
Calls: service_order
Why: separates orchestration from HTTP.
Without: impossible to evolve business logic independently.
Step: added in STEP-1.
"""
from app.features.orders.services.service_order import service_order
def handle_order(value: str) -> dict[str,str]:
    """Coordinate one input value and map a stable response contract."""
    return {"status": "accepted", "detail": service_order(value)}
