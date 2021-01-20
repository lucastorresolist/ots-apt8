from sqlalchemy import Column, String
from .base_model import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'

    name = Column(String(length=100))
    description = Column(String(length=150))
    price = Column(String(length=15))

    def __init__(self, name: str, description: str, price: str):
        self.name = name
        self.description = description
        self.price = price

