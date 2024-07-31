from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import health, history

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(history.router)
app.include_router(health.router)
