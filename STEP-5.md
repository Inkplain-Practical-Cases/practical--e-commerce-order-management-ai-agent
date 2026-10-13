# STEP-5 — Reliability and review policy

New source implements bounded retry, authorization, idempotency or human review policy, depending on the business domain. Branch inherits STEP-4; run `python -m pytest -q`. STEP-6 combines and hardens deployment and CI.

## Database (Entity) Relations
STEP-5 retains unchanged the SQLite `orders` table defined in `app/features/orders/providers/order_repository.py`: `id TEXT PRIMARY KEY`, `buyer TEXT NOT NULL`, `sku TEXT NOT NULL`, `quantity INTEGER NOT NULL CHECK(quantity>0)`. No persisted inventory table or foreign key exists. See `STEP-5.erd` and the main `.inkp` tab `STEP-5-ERD`.
