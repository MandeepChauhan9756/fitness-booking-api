from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# -----------------------------
# Authentication Schemas
# -----------------------------

class UserSignup(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    

# -----------------------------
# User Response
# -----------------------------

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)
    
    
# -----------------------------
# Fitness Class Schemas
# -----------------------------

class FitnessClassCreate(BaseModel):
    name: str
    instructor: str
    date_time: datetime
    available_slots: int = Field(..., gt=0)
    
    
class FitnessClassResponse(BaseModel):
    id: int
    name: str
    instructor: str
    date_time: datetime
    available_slots: int
    
    model_config = ConfigDict(from_attributes=True)
    
    
# -----------------------------
# Booking Schemas
# -----------------------------

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr
    
    
class BookingResponse(BaseModel):
    id: int
    class_name: str
    instructor: str
    date_time: datetime
    client_name: str
    client_email: EmailStr
    booked_at: datetime
    
    model_config = ConfigDict(from_attributes=True)