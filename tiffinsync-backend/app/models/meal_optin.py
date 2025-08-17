from sqlalchemy import Column, ForeignKey, Enum, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint
import uuid
import enum

from app.database import Base

class MealOptinStatus(enum.Enum):
    opted_in = "opted_in"
    opted_out = "opted_out"

class MealOptin(Base):
    __tablename__ = "meal_optins"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    meal_id = Column(UUID(as_uuid=True), ForeignKey("meals.id", ondelete="CASCADE"), nullable=False)
    status = Column(Enum(MealOptinStatus), nullable=False)
    date = Column(Date, nullable=False)

    # Relationships
    user = relationship("User", back_populates="meal_optins")
    meal = relationship("Meal", back_populates="meal_optins")
    __table_args__ = (
        UniqueConstraint('user_id', 'meal_id', name='unique_user_meal_optin'),
    )

