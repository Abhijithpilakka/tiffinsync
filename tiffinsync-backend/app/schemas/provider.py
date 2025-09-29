from pydantic import BaseModel
from typing import Optional

class ProviderCreate(BaseModel):
    delivery_radius: float
    latitude: float
    longitude: float

class ProviderResponse(BaseModel):
    id: str   # UUID as string
    user_id: str
    delivery_radius: float
    latitude: float
    longitude: float
    name: str
    address: Optional[str] = None

    class Config:
        from_attributes = True