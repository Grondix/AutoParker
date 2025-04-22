from fastapi import FastAPI
from order_service.routes import order_routes

app = FastAPI()
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
