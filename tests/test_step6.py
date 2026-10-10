import sqlite3
from app.features.orders.services.end_to_end import submit_demo_order

def test_idempotent_submission():
    conn=sqlite3.connect(":memory:")
    first=submit_demo_order(conn,"buyer-final","SKU-101",1,"key-final")
    second=submit_demo_order(conn,"buyer-final","SKU-101",1,"key-final")
    assert first==second
    assert conn.execute("SELECT count(*) FROM orders").fetchone()[0]==1
