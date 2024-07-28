from sqlalchemy.orm import Session
from ..models.history import History
from ..schemas.history import HistoryCreate
from ..llm.gemini import generate_bot_response

def create_history(db: Session, history: HistoryCreate):
    bot_response = generate_bot_response(history.user_message)

    db_history = History(user_message=history.user_message, bot_response=bot_response, feedback=False)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)

    return db_history