from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Provider
from app.schemas.user import UserRegister, UserResponse, OTPRequest, OTPVerify
from app.utils.auth_utils import hash_password, create_access_token
from app.utils.otp import generate_mock_otp, verify_mock_otp
import uuid

router = APIRouter(prefix="/auth", tags=["Auth"])

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
    if not verify_mock_otp(data.phone, data.otp):
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    user = db.query(User).filter(User.phone == data.phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    access_token = create_access_token({"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
