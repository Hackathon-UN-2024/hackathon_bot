from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.history import History, HistoryCreate
from ..crud.history import create_history, get_history
from ..core.database import get_db

router = APIRouter()

@router.post("/histories/", response_model=History)
def create_new_history(history: HistoryCreate, db: Session = Depends(get_db)):
    return create_history(db, history)

@router.get("/histories/{history_id}", response_model=History)
def read_history(history_id: int, db: Session = Depends(get_db)):
    history = get_history(db, history_id)
    if history is None:
        raise HTTPException(status_code=404, detail="History not found")
    return history