from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Subscription, User, Provider
from app.dependencies.auth import get_current_user
from app.schemas.subscriptions import SubscriptionResponse

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------
# Subscribe to a Provider
# ----------------------
@router.post("/{provider_id}", response_model=SubscriptionResponse)
def subscribe(
    provider_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="Only users can subscribe")

    provider = db.query(Provider).filter(Provider.id == provider_id).first()
    if not provider:
        raise HTTPException(status_code=404, detail="Provider not found")

    existing = db.query(Subscription).filter(
        Subscription.user_id == current_user.id,
        Subscription.provider_id == provider_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already subscribed to this provider")

    subscription = Subscription(user_id=current_user.id, provider_id=provider_id)
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription


# ----------------------
# Unsubscribe from Provider
# ----------------------
@router.delete("/{provider_id}")
def unsubscribe(
    provider_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="Only users can unsubscribe")

    subscription = db.query(Subscription).filter(
        Subscription.user_id == current_user.id,
        Subscription.provider_id == provider_id
    ).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    db.delete(subscription)
    db.commit()
    return {"detail": "Unsubscribed successfully"}


# ----------------------
# Get My Subscriptions (User)
# ----------------------
@router.get("/me", response_model=list[SubscriptionResponse])
def get_my_subscriptions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="Only users can view their subscriptions")

    subscriptions = db.query(Subscription).filter(Subscription.user_id == current_user.id).all()
    return subscriptions


# ----------------------
# Get Subscribers (Provider)
# ----------------------
@router.get("/provider", response_model=list[SubscriptionResponse])
def get_my_subscribers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "provider":
        raise HTTPException(status_code=403, detail="Only providers can view subscribers")

    provider = db.query(Provider).filter(Provider.user_id == current_user.id).first()
    if not provider:
        raise HTTPException(status_code=404, detail="Provider profile not found")

    subscriptions = db.query(Subscription).filter(Subscription.provider_id == provider.id).all()
    return subscriptions