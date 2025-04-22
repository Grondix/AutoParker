from fastapi import FastAPI
from vehicle_service.routes import vehicle_routes

app = FastAPI()
app.include_router(vehicle_routes.router, prefix="/vehicles", tags=["Vehicles"])
