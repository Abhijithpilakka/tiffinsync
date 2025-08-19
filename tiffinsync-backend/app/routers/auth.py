from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Provider
from app.schemas.user import UserRegister, UserResponse, OTPRequest, OTPVerify
from app.utils.auth_utils import hash_password, create_access_token, create_refresh_token, verify_token
from app.utils.otp import generate_mock_otp, verify_mock_otp
from app.schemas.user import (
    OTPRequest, OTPVerify,
    TokenResponse, RefreshTokenRequest, AccessTokenResponse
)
from app.utils.auth_utils import create_access_token, create_refresh_token, verify_token
import uuid
import os

router = APIRouter(prefix="/auth", tags=["Auth"])

JWT_REFRESH_SECRET = os.getenv("JWT_REFRESH_SECRET")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.phone == user_data.phone).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone already registered")

    hashed_password = hash_password(user_data.password) if user_data.password else None

    new_user = User(
        id=uuid.uuid4(),
        name=user_data.name,
        phone=user_data.phone,
        email=user_data.email,
        password=hashed_password,
        role=user_data.role,
        address=user_data.address,
        latitude=user_data.latitude,
        longitude=user_data.longitude,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    if user_data.role == "provider":
        if not user_data.delivery_radius:
            raise HTTPException(status_code=400, detail="Delivery radius required for providers")

        new_provider = Provider(
            user_id=new_user.id,
            delivery_radius=user_data.delivery_radius
        )
        db.add(new_provider)
        db.commit()

    return new_user

@router.post("/send-otp")
def send_otp(data: OTPRequest):
    otp = generate_mock_otp(data.phone)
    return {"message": "OTP sent successfully (mocked)"}

@router.post("/verify-otp")
def verify_otp(data: OTPVerify, db: Session = Depends(get_db)):
    phone = data.phone
    otp = data.otp

    if not verify_mock_otp(phone, otp):
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    # Check if user exists
    user = db.query(User).filter(User.phone == phone).first()

    if not user:
        # Auto-register new user
        new_user = User(
            id=uuid.uuid4(),
            name="New User",        # 👈 you can later update via profile
            phone=phone,
            role="user",            # 👈 default role
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        user = new_user

    # Create JWT tokens
    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": {
            "id": str(user.id),
            "name": user.name,
            "phone": user.phone,
            "role": user.role.value if user.role else None,
        }
    }

@router.post("/refresh", response_model=AccessTokenResponse)
def refresh_token(payload: RefreshTokenRequest):
    token_payload = verify_token(payload.refresh_token, JWT_REFRESH_SECRET)
    if not token_payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token({"sub": token_payload["sub"]})
    return {"access_token": new_access_token, "token_type": "bearer"}
