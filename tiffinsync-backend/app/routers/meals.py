from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.meal import Meal
from app.schemas.meal import MealCreate, MealResponse

router = APIRouter(prefix="/meals", tags=["Meals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MealResponse)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    new_meal = Meal(**meal.dict())
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

@router.get("/", response_model=list[MealResponse])
def get_meals(db: Session = Depends(get_db)):
    return db.query(Meal).all()
