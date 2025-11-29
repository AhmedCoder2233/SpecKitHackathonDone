# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.db import init_db
import os

app = FastAPI(
    title="FastAPI Backend",
    description="Backend for authentication and user management",
    version="1.0.0"
)

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()
    print("Database tables created/verified!")

@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running!"}

# Include API routers
from src.api import auth
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])