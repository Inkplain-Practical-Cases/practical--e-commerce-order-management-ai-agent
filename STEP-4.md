# STEP 4 — Reserve synthetic inventory

Atomic local reservation, positive quantity and insufficient-stock checks. A durable PostgreSQL transaction is not yet implemented. Run `python -m pytest -q`.

## Database (Entity) Relations
STEP-4 retains unchanged the SQLite `orders` table defined in `app/features/orders/providers/order_repository.py`: `id TEXT PRIMARY KEY`, `buyer TEXT NOT NULL`, `sku TEXT NOT NULL`, `quantity INTEGER NOT NULL CHECK(quantity>0)`. No persisted inventory table or foreign key exists. See `STEP-4.erd` and the main `.inkp` tab `STEP-4-ERD`.
