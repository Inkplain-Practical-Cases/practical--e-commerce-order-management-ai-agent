# STEP 6 of 6 — Integrate and harden orders

Install dependencies, run `python -m pytest -q`, and start `uvicorn app.main:app`. The full cumulative implementation provides tested local domain behavior and deterministic fixtures. The teaching code does **not** imply production approval, live services or all external adapters are complete. Audit the README limitations before deployment.

## Database (Entity) Relations
STEP-6 retains unchanged the SQLite `orders` table defined in `app/features/orders/providers/order_repository.py`: `id TEXT PRIMARY KEY`, `buyer TEXT NOT NULL`, `sku TEXT NOT NULL`, `quantity INTEGER NOT NULL CHECK(quantity>0)`. No persisted inventory table or foreign key exists. See `STEP-6.erd` and the main `.inkp` tab `STEP-6-ERD`.
