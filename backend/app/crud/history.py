from sqlalchemy.orm import Session
from ..models.history import History
from ..schemas.history import HistoryCreate

def create_history(db: Session, history: HistoryCreate):
    db_history = History(user_message=history.user_message, bot_response=history.bot_response, feedback=history.feedback)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

def get_history(db: Session, history_id: int):
    return db.query(History).filter(history_id == History.id).first()