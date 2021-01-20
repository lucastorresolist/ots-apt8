from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Seller:
    __tablename__ = 'seller'

    id = Column( Integer, primary_key=True )
    name = Column( String(length=100) )
    telephone = Column( String(length=20) )
    email = Column( String(length=50) )

    def __init__(self, name:str, telephone:str, email: str, id: str = None) -> None:
        self.__name = name
        self.__telephone = telephone
        self.__email = email
        self.__id = id

    @property
    def id(self)-> int:
        return self.__id

    @property
    def name(self)-> str:
        return self.__name

    @property
    def telephone(self)-> str:
        return self.__telephone

    @property
    def email(self)-> str:
        return self.__email

    @id.setter
    def id(self, id)-> None:
        self.__id = id

    @name.setter
    def name(self, name)-> None:
        self.__name = name

    @telephone.setter
    def telephone(self, phone)-> None:
        self.__telephone = phone

    @email.setter
    def email(self, email)-> None:
        self.__email = email
