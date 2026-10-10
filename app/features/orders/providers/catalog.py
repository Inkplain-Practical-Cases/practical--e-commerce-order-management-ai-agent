"""Fake inventory read provider, deterministic for offline exercises."""
CATALOG={"SKU-101":{"sku":"SKU-101","stock":8,"currency":"EUR"},"SKU-202":{"sku":"SKU-202","stock":0,"currency":"EUR"}}

def lookup_product(sku:str)->dict|None:
    """Read trusted catalog snapshot; never mutate stock in STEP-2."""
    return CATALOG.get(sku.strip())
