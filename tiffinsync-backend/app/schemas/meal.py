from pydantic import BaseModel

class MealCreate(BaseModel):
    type: str
    description: str
    provider_id: int

class MealResponse(BaseModel):
    id: int
    type: str
    description: str

    class Config:
        orm_mode = True
