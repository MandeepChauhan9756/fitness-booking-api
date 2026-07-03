# Fitness Booking API

A RESTful Booking API built using **FastAPI** that allows users to register, authenticate, create fitness classes, book available classes, and view their bookings. The project was developed as part of a Backend Developer Intern assignment with a focus on clean architecture, authentication, validation, and modular code organization.

---

## Features

1. User Registration (Sign Up)
2. User Login with JWT Authentication
3. Create Fitness Classes (Authenticated)
4. View Upcoming Fitness Classes
5. Book Available Fitness Classes
6. View Bookings of the Authenticated User
7. Prevent Duplicate Bookings
8. Prevent Overbooking
9. Automatic Slot Deduction After Successful Booking
10. Timezone Handling (IST)
11. Request Validation using Pydantic
12. Custom Exception Handling
13. Request Logging Middleware
14. Interactive Swagger Documentation

---

## Tech Stack

1. **Language:** Python 3.12
2. **Framework:** FastAPI
3. **Database:** SQLite
4. **ORM:** SQLAlchemy
5. **Authentication:** JWT (JSON Web Token)
6. **Validation:** Pydantic
7. **Password Hashing:** Passlib (bcrypt)
8. **API Testing:** Postman

---

## Project Structure

```text
fitness-booking-api/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── classes.py
│   │   └── bookings.py
│   │
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── middleware.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
│
├── postman/
│   └── Fitness Booking API.postman_collection.json
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd fitness-booking-api
```

---

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Create a `.env` file in the project root and copy the values from `.env.example`.

Example:

```env
APP_NAME=Fitness Booking API
APP_VERSION=1.0.0

DATABASE_URL=sqlite:///./fitness.db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 5. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Authentication

| Method | Endpoint  | Description                 |
| ------ | --------- | --------------------------- |
| POST   | `/signup` | Register a new user         |
| POST   | `/login`  | Login and receive JWT token |

---

### Fitness Classes

| Method | Endpoint   | Description                                      |
| ------ | ---------- | ------------------------------------------------ |
| POST   | `/classes` | Create a fitness class (Authentication Required) |
| GET    | `/classes` | Get all upcoming fitness classes                 |

---

### Bookings

| Method | Endpoint | Description                                    |
| ------ | -------- | ---------------------------------------------- |
| POST   | `/book`  | Book a fitness class (Authentication Required) |
| GET    | `/book`  | View bookings of the authenticated user        |

---

### Health Check

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | `/health` | Check API status |

---

## Authentication

Protected endpoints require a JWT token.

After logging in, copy the access token returned by the API.

Include it in the request header:

```text
Authorization: Bearer <your_access_token>
```

---

## Validation & Error Handling

The application handles several validation scenarios, including:

1. Missing required fields
2. Invalid email format
3. Invalid or expired JWT token
4. Duplicate user registration
5. Duplicate class booking
6. Booking when no slots are available
7. Booking a class that has already started

---

## Timezone Handling

All fitness class timings are stored and managed in **Indian Standard Time (IST)**.

Timezone-aware datetime values are accepted and converted to IST before storing them.

---

## Postman Collection

A Postman collection is included inside the `postman/` directory for testing all available API endpoints.

---

## Author

**Mandeep Chauhan**

Backend Developer | Python | FastAPI | SQLAlchemy
