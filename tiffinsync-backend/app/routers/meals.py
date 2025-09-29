from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Meal, User, Provider
from app.schemas.meal import MealCreate, MealResponse
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/meals", tags=["Meals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------
# Create Meal (Provider)
# ----------------------
@router.post("/", response_model=MealResponse)
def create_meal(
    meal: MealCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "provider":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only providers can create meals",
        )

    provider = db.query(Provider).filter(Provider.user_id == current_user.id).first()
    if not provider:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provider profile not found",
        )

    new_meal = Meal(**meal.dict(), provider_id=provider.id)
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal


# ----------------------
# Get All Meals
# ----------------------
@router.get("/", response_model=list[MealResponse])
def get_meals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role == "provider":
        provider = db.query(Provider).filter(Provider.user_id == current_user.id).first()
        return db.query(Meal).filter(Meal.provider_id == provider.id).all()

    return db.query(Meal).all()


# ----------------------
# Get Meal by ID
# ----------------------
@router.get("/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: str, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    return meal


# ----------------------
# Update Meal (Provider)
# ----------------------
@router.put("/{meal_id}", response_model=MealResponse)
def update_meal(
    meal_id: str,
    meal_update: MealCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "provider":
        raise HTTPException(status_code=403, detail="Only providers can update meals")

    provider = db.query(Provider).filter(Provider.user_id == current_user.id).first()
    meal = db.query(Meal).filter(Meal.id == meal_id, Meal.provider_id == provider.id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")

    for key, value in meal_update.dict().items():
        setattr(meal, key, value)

    db.commit()
    db.refresh(meal)
    return meal


# ----------------------
# Delete Meal (Provider)
# ----------------------
@router.delete("/{meal_id}", status_code=204)
def delete_meal(
    meal_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "provider":
        raise HTTPException(status_code=403, detail="Only providers can delete meals")

    provider = db.query(Provider).filter(Provider.user_id == current_user.id).first()
    meal = db.query(Meal).filter(Meal.id == meal_id, Meal.provider_id == provider.id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")

    db.delete(meal)
    db.commit()
    return {"detail": "Meal deleted"}