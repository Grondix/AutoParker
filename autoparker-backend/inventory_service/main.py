from fastapi import FastAPI
from inventory_service.routes import inventory_routes

app = FastAPI()
app.include_router(inventory_routes.router, prefix="/inventory", tags=["Inventory"])
