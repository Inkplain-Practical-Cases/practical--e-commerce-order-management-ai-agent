"""HTTP door: validate typed request and delegate to handler.
ICS layer: door
CRD component: be.receive_order
Called by: REST clients
Calls: handle_order
Why: keeps HTTP and business rules separate.
Without: validation and orchestration become coupled.
Step: added in STEP-1.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.features.orders.handlers.handle_order import handle_order
router = APIRouter(prefix="/api", tags=["orders"])
class OrderRequest(BaseModel):
    product_sku: str = Field(min_length=3, max_length=2500)
class OrderResponse(BaseModel):
    status: str
    detail: str
@router.post("/orders", response_model=OrderResponse)
def receive_order(request: OrderRequest) -> OrderResponse:
    # Every request is validated before the handler sees it.
    return OrderResponse(**handle_order(request.product_sku))
