# STEP-3 of 6 — Domain state and logic

STEP-3 implements runnable local transactional persistence through SQLite for deterministic tests. True PostgreSQL-backed adapter remains an explicit open requirement, not silently claimed done.

This branch inherits STEP-2's code and tests. The new functions are intentionally isolated for test-driven learning. Use `python -m pytest -q` to exercise old and new behavior; unresolved later-stage integration is explicitly documented instead of claimed complete.

## Database (Entity) Relations
STEP-3 introduces the SQLite `orders` table defined in `app/features/orders/providers/order_repository.py`: `id TEXT PRIMARY KEY`, `buyer TEXT NOT NULL`, `sku TEXT NOT NULL`, `quantity INTEGER NOT NULL CHECK(quantity>0)`. No persisted inventory table or foreign key exists. See `STEP-3.erd` and the main `.inkp` tab `STEP-3-ERD`.
