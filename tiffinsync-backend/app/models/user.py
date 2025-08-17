from sqlalchemy import Column, String, Float, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum

from app.database import Base

class UserRole(enum.Enum):
    user = "user"
    provider = "provider"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=True)  # nullable for Google OAuth
    role = Column(Enum(UserRole), nullable=False)
    address = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    provider = relationship("Provider", back_populates="user", uselist=False)
    subscriptions = relationship("Subscription", back_populates="user", cascade="all, delete-orphan")
    meal_optins = relationship("MealOptin", back_populates="user", cascade="all, delete-orphan")

