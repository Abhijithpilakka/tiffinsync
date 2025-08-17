from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Provider
from app.schemas.provider import ProviderCreate, ProviderResponse
from app.models import Subscription
from app.dependencies.auth import get_current_user

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
def subscribe_to_provider(provider_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
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