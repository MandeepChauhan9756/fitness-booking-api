from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.models import Booking, FitnessClass, User
from app.schemas import BookingCreate, BookingResponse
from app.utils import get_current_ist, ensure_ist

router = APIRouter(
    prefix="/book",
    tags=["Bookings"],
)


@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def book_class(booking: BookingCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Check class exists
    fitness_class = (db.query(FitnessClass).filter(FitnessClass.id == booking.class_id).first())
    
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Fitness class not found")
    
    # Prevent duplicate booking
    existing_booking = (db.query(Booking).filter(
        Booking.user_id == current_user.id,
        Booking.class_id == booking.class_id,
    ).first())
    
    if existing_booking:
        raise HTTPException(status_code=400, detail="You have already booked this class.")
    
    # Check available slots
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available.")
    
    class_time = ensure_ist(fitness_class.date_time)
    if class_time < get_current_ist():
        raise HTTPException(status_code=400, detail="Cannot book a class that has already started.")
    
    # Create Booking
    new_booking = Booking(
        user_id = current_user.id,
        class_id = booking.class_id,
        client_name = booking.client_name,
        client_email = booking.client_email,
    )
    
    # Reduce slot count
    fitness_class.available_slots -= 1
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {
        "id": new_booking.id,
        "class_name": fitness_class.name,
        "instructor": fitness_class.instructor,
        "date_time": fitness_class.date_time,
        "client_name": new_booking.client_name,
        "client_email": new_booking.client_email,
        "booked_at": new_booking.booked_at,
    }


@router.get("", response_model=list[BookingResponse])
def get_my_bookings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    bookings = (db.query(Booking).filter(Booking.user_id == current_user.id).all())
    return [
        {
            "id": booking.id,
            "class_name": booking.fitness_class.name,
            "instructor": booking.fitness_class.instructor,
            "date_time": booking.fitness_class.date_time,
            "client_name": booking.client_name,
            "client_email": booking.client_email,
            "booked_at": booking.booked_at,
        }
        for booking in bookings
    ]