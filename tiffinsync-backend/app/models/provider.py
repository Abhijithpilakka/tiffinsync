from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class Provider(Base):
    __tablename__ = "providers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    delivery_radius = Column(Float, nullable=False)  # in km

    # Relationships
    user = relationship("User", back_populates="provider")
    meals = relationship("Meal", back_populates="provider", cascade="all, delete-orphan")
    subscriptions = relationship("Subscription", back_populates="provider", cascade="all, delete-orphan")

