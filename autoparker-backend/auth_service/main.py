from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from shared.database import create_db_and_tables
from auth_service.routes import auth_routes, user_routes, role_routes
from shared.utils.init_admin import create_initial_admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(role_routes.router, prefix="/roles", tags=["Roles"])

@app.on_event("startup")
def startup():
    create_db_and_tables()
    create_initial_admin()
