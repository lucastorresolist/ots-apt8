from sqlalchemy import Column, String, DateTime
from .base_model import BaseModel
from sqlalchemy.sql import func


class Log(BaseModel):
    __tablename__ = 'logs'
    data = Column(DateTime(timezone=True), default=func.now())
    action = Column( String(length=100) )
    type = Column( String(length=100) )

    def __init__(self, action:str, type:str)-> None:
        self.action = action
        self.type = type
