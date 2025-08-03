from pydantic import BaseModel

class ProviderCreate(BaseModel):
    name: str
    location: str

class ProviderResponse(BaseModel):
    id: int
    name: str
    location: str
    rating: int

    class Config:
        orm_mode = True
