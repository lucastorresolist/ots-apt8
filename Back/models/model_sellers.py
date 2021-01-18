class Seller:

    def __init__(self, name:str, phone:str, email:str, id:int = None)-> None:
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__email = email

    @property
    def id(self)-> int:
        return self.__id

    @property
    def name(self)-> str:
        return self.__name

    @property
    def phone(self)-> str:
        return self.__phone

    @property
    def email(self)-> str:
        return self.__email

    @id.setter
    def id(self, id)-> None:
        self.__id = id

    @name.setter
    def name(self, name)-> None:
        self.__name = name

    @phone.setter
    def phone(self, phone)-> None:
        self.__phone = phone

    @email.setter
    def email(self, email)-> None:
        self.__email = email
