# shared/schemas/order_schemas.py
from pydantic import BaseModel
from typing import Optional, List

class OrderCreate(BaseModel):
    name: str
    description: Optional[str] = None

class OrderItem(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str

    class Config:
        orm_mode = True
