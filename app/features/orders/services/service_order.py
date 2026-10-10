"""STEP-2 order service: validate catalog SKU and stock, never trust client prices."""
from app.features.orders.providers.catalog import lookup_product

def service_order(value:str)->str:
    """Return a catalog stock check for an approved SKU (no order persisted yet)."""
    product=lookup_product(value)
    if product is None:return "SKU unavailable; input length: "+str(len(value))
    return "SKU "+product["sku"]+"; stock "+str(product["stock"])+"; currency "+product["currency"]
