"""Atomic in-memory stock reservation for local learning fixtures."""
from threading import Lock
_lock=Lock()
_stock={"SKU-101":8,"SKU-202":0}

def reserve_stock(sku:str,quantity:int)->dict:
    """Reject non-positive quantities and stock overselling."""
    if quantity<=0:raise ValueError("Positive quantity required")
    with _lock:
        available=_stock.get(sku,0)
        if available<quantity:raise ValueError("Insufficient stock")
        _stock[sku]-=quantity
        return {"sku":sku,"reserved":quantity,"remaining":_stock[sku]}
