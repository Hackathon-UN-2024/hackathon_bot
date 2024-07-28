from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.history import History, HistoryCreate
from ..crud.history import create_history
from ..core.database import get_db

router = APIRouter()

@router.post("/histories/", response_model=History)
def create_new_history(history: HistoryCreate, db: Session = Depends(get_db)):
    return create_history(db, history)