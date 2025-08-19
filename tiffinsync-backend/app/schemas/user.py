from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    user = "user"
    provider = "provider"

class UserRegister(BaseModel):
    name: str
    phone: str
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: UserRole
    address: str
    latitude: float
    longitude: float
    delivery_radius: Optional[float] = None  # only for provider

class UserResponse(BaseModel):
    id: str
    name: str
    phone: str
    email: Optional[EmailStr] = None
    role: UserRole
    address: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True

class OTPRequest(BaseModel):
    phone: str

class OTPVerify(BaseModel):
    phone: str
    otp: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"