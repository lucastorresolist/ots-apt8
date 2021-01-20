from Back.models.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class Seller(BaseModel):
    __tablename__ = 'sellers'

    name = Column( String(length=50) )
    phone = Column( String(length=50) )
    email = Column( String(length=50) )

    def __init__(self, name:str, phone:str, email: str, id: str = None) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id
