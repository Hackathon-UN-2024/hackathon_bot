from sqlalchemy import Column, Integer, String, Boolean
from ..core.database import Base

class History(Base):
    __tablename__ = "histories"
    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(String, index=True)
    bot_response = Column(String, index=True)
    feedback = Column(Boolean, index=True)
