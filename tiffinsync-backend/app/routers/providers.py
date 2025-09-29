from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Provider
from app.schemas.provider import ProviderCreate, ProviderResponse
from app.models import Subscription
from app.dependencies.auth import get_current_user
from math import radians, sin, cos, sqrt, atan2
from app.models import User  # for nearby providers
from uuid import UUID

router = APIRouter(prefix="/providers", tags=["Providers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProviderResponse)
def create_provider(provider: ProviderCreate, db: Session = Depends(get_db)):
    new_provider = Provider(**provider.dict())
    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)
    return new_provider

@router.get("/", response_model=list[ProviderResponse])
def get_providers(db: Session = Depends(get_db)):
    return db.query(Provider).all()


@router.post("/subscribe/{provider_id}")
def subscribe_to_provider(provider_id: UUID, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    provider = db.query(Provider).filter(Provider.id == provider_id).first()
    if not provider:
        raise HTTPException(status_code=404, detail="Provider not found")

    subscription = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()

    if subscription:
        subscription.provider_id = provider_id
        subscription.is_active = True
    else:
        subscription = Subscription(user_id=current_user.id, provider_id=provider_id)
        db.add(subscription)

    db.commit()
    return {"message": f"Subscribed to {provider.name}"}

@router.get("/my-subscription")
def get_user_subscription(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    subscription = db.query(Subscription).filter(Subscription.user_id == current_user.id, Subscription.is_active == True).first()

    if not subscription:
        return {"subscribed": False}

    provider = db.query(Provider).filter(Provider.id == subscription.provider_id).first()

    return {
        "subscribed": True,
        "provider": provider
    }



# Haversine formula for distance between two lat/lon points
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in km

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c  # in kilometers


# ----------------------
# Nearby Providers
# ----------------------
@router.get("/nearby", response_model=list[ProviderResponse])
def get_nearby_providers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="Only users can view nearby providers")

    if not current_user.latitude or not current_user.longitude:
        raise HTTPException(status_code=400, detail="User location not set")

    providers = db.query(Provider).all()
    nearby = []

    for provider in providers:
        provider_user = db.query(User).filter(User.id == provider.user_id).first()
        if not provider_user or not provider_user.latitude or not provider_user.longitude:
            continue

        distance = calculate_distance(
            current_user.latitude,
            current_user.longitude,
            provider_user.latitude,
            provider_user.longitude,
        )

        if distance <= provider.delivery_radius:
            nearby.append(ProviderResponse(
                id=str(provider.id),
                name=provider_user.name,
                address=provider_user.address,
                latitude=provider_user.latitude,
                longitude=provider_user.longitude,
                delivery_radius=provider.delivery_radius
            ))

    return nearby