import sqlite3
from app.features.orders.providers.order_repository import init_database,create_order

def test_order_atomic_insert():
    db=sqlite3.connect(":memory:");init_database(db)
    oid=create_order(db,"buyer-a","SKU-101",2)
    assert db.execute("SELECT buyer FROM orders WHERE id=?",(oid,)).fetchone()[0]=="buyer-a"
def test_invalid_quantity():
    import pytest
    db=sqlite3.connect(":memory:");init_database(db)
    with pytest.raises(ValueError):create_order(db,"buyer-a","SKU-101",-1)
