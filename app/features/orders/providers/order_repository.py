"""SQLite transaction simulation for STEP-3; PostgreSQL production adapter is a later migration.
ICS provider; component be.order_repository. Uses standard sqlite3 for local reproducibility.
"""
import sqlite3
from uuid import uuid4

def init_database(conn:sqlite3.Connection)->None:
    conn.execute("CREATE TABLE IF NOT EXISTS orders(id TEXT PRIMARY KEY, buyer TEXT NOT NULL, sku TEXT NOT NULL, quantity INTEGER NOT NULL CHECK(quantity>0))")
    conn.commit()

def create_order(conn:sqlite3.Connection,buyer:str,sku:str,quantity:int)->str:
    """Commit a single order or roll back; no inventory reservation until STEP-4."""
    if not buyer or quantity<=0:raise ValueError("buyer required; quantity positive")
    order_id=uuid4().hex
    with conn:
        conn.execute("INSERT INTO orders(id,buyer,sku,quantity) VALUES (?,?,?,?)",(order_id,buyer,sku,quantity))
    return order_id
