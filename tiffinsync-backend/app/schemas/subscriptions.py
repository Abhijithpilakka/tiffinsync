from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


# ----------------------
# Base Schema
# ----------------------
class SubscriptionBase(BaseModel):
    user_id: UUID
    provider_id: UUID
    is_active: bool = True


# ----------------------
# For Creating Subscription
# ----------------------
class SubscriptionCreate(BaseModel):
    provider_id: UUID


# ----------------------
# Response Schema
# ----------------------
class SubscriptionResponse(SubscriptionBase):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True