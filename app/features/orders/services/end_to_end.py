"""Starter end-to-end safe order submission in a local teaching fixture."""
import sqlite3
from app.features.orders.providers.catalog import lookup_product
from app.features.orders.providers.order_repository import init_database,create_order
from app.features.orders.services.idempotency import run_idempotent
from app.features.orders.services.inventory_reservation import reserve_stock

def submit_demo_order(conn:sqlite3.Connection,buyer:str,sku:str,quantity:int,key:str)->dict:
    """Reject invalid catalog entries; deduplicate a local order request."""
    product=lookup_product(sku)
    if not product or quantity<=0:raise ValueError("Invalid order")
    init_database(conn)
    def create():
        # Educational limitation: reservations are in-memory and DB writes are not one distributed transaction.
        reservation=reserve_stock(sku,quantity)
        order_id=create_order(conn,buyer,sku,quantity)
        return {"order_id":order_id,"reservation":reservation}
    return run_idempotent(buyer,key,f"{sku}:{quantity}",create)
