from app.features.orders.services.inventory_reservation import reserve_stock
import pytest
def test_valid_reservation():
    assert reserve_stock("SKU-101",1)["reserved"]==1
def test_no_oversell():
    with pytest.raises(ValueError):reserve_stock("SKU-202",1)
