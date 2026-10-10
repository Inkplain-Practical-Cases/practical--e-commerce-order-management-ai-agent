from app.features.orders.services.idempotency import run_idempotent
import pytest
def test_deduplicates_write():
    count=[0]
    def create():count[0]+=1;return "order1"
    assert run_idempotent("buyer-x","key-1","sku101",create)=="order1"
    assert run_idempotent("buyer-x","key-1","sku101",create)=="order1"
    assert count[0]==1
def test_conflict_fails():
    with pytest.raises(ValueError):run_idempotent("buyer-x","key-1","changed",lambda:"order2")
