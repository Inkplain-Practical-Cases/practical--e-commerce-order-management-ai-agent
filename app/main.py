"""FastAPI composition root: register HTTP door only."""
from fastapi import FastAPI
from app.features.orders.router import router
app = FastAPI(title="Order Starter Practical Case")
app.include_router(router)
