from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User

from app.schemas.user import UserCreate, UserResponse
from app.utils.auth_utils import hash_password, verify_password, create_access_token, create_refresh_token, verify_token
import os

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(name=user.name, email=user.email, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "access_token": create_access_token({"user_id": user.id}),
        "refresh_token": create_refresh_token({"user_id": user.id})
    }

@router.post("/refresh")
def refresh(refresh_token: str):
    payload = verify_token(refresh_token, secret=os.getenv("JWT_REFRESH_SECRET"))
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
    return {"access_token": create_access_token({"user_id": payload["user_id"]})}
