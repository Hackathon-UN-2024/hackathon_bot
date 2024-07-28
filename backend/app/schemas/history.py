from pydantic import BaseModel

class HistoryBase(BaseModel):
    user_message: str
    bot_response: str
    feedback: bool

class HistoryCreate(HistoryBase):
    pass

class History(HistoryBase):
    id: int

    class Config:
        orm_mode = True