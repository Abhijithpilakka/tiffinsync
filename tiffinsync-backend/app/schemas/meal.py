from pydantic import BaseModel
from datetime import date
from typing import Optional

class MealCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    date: date

class MealResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    price: float
    date: date
    provider_id: str  # still returned in response

    class Config:
        from_attributes = True