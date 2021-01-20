class Product:

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @description.setter
    def description(self, description):
        self.__description = description

    @price.setter
    def price(self, price):
        self.__price = price