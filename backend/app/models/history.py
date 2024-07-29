from sqlalchemy import Column, BigInteger, Text, Boolean
from ..core.database import Base

class History(Base):
    __tablename__ = "histories"
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    user_message = Column(Text, index=True)
    bot_response = Column(Text, index=True)
    feedback = Column(Boolean, index=True)
