from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    provider_id = Column(Integer, ForeignKey("providers.id"))
