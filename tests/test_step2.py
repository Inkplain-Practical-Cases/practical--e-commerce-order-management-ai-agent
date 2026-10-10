from app.features.orders.providers.catalog import lookup_product
from app.features.orders.services.service_order import service_order

def test_available_stock_read():
    assert lookup_product("SKU-101")["stock"]==8
    assert "stock 8" in service_order("SKU-101")
def test_unknown_sku():
    assert lookup_product("missing") is None
