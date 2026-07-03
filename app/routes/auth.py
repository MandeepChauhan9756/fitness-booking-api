from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth import (create_access_token, hash_password, verify_password)
from app.database import get_db
from app.models import User
from app.schemas import Token, UserLogin, UserResponse, UserSignup

router = APIRouter(tags=["Authentication"])

@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    existing_user = (db.query(User).filter(User.email == user.email).first())
    
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    
    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = hash_password(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = (db.query(User).filter(User.email == user.email).first())
    
    if (not existing_user or not verify_password(user.password, existing_user.hashed_password)):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": existing_user.email})
    return {"access_token": access_token, "token_type": "bearer"}