# from datetime import timezone, datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.models import FitnessClass, User
from app.schemas import FitnessClassCreate, FitnessClassResponse
from app.utils import convert_to_ist, get_current_ist

router = APIRouter(
    prefix="/classes",
    tags=["Fitness Classes"],
)

@router.post("", response_model=FitnessClassResponse, status_code=status.HTTP_201_CREATED)
def create_class(fitness_class: FitnessClassCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if fitness_class.date_time.tzinfo is None:
        raise HTTPException(status_code=404, detail="date_time must contain timezone information.")
    
    new_class = FitnessClass(
        name = fitness_class.name,
        instructor = fitness_class.instructor,
        date_time = convert_to_ist(fitness_class.date_time),
        available_slots = fitness_class.available_slots,
    )
    
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    
    return new_class


@router.get("", response_model=list[FitnessClassResponse])
def get_classes(db: Session = Depends(get_db)):
    classes = (db.query(FitnessClass).filter(FitnessClass.date_time >= get_current_ist()).order_by(FitnessClass.date_time.asc()).all())
    
    return classes