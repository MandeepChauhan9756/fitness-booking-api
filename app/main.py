from fastapi import FastAPI
# from app.database import Base, engine
from app.models import User
from fastapi import Depends
from app.dependencies import get_current_user
from app.routes import auth, bookings, classes
from app.exceptions import register_exception_handlers
from app.middleware import log_requests

# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fitness booking API",
    version="1.0.0",
)

register_exception_handlers(app)
app.middleware("http")(log_requests)

app.include_router(auth.router)
app.include_router(classes.router)
app.include_router(bookings.router)

@app.get("/")
def root():
    return {
        "message": "Fitness Booking API is running"
    }

@app.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }