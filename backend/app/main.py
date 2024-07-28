from fastapi import FastAPI
from .routers import health, history

app = FastAPI()

app.include_router(history.router)
app.include_router(health.router)
