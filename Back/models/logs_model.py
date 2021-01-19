class Log:

    def __init__(self, action: str, type: str, data: str = None, id: int = None) -> None:
        self.__data = data
        self.__action = action
        self.__type = type
        self.__id = id

    @property
    def data(self):
        return self.__data

    @property
    def action(self):
        return self.__action

    @property
    def type(self):
        return self.__type

    @property
    def id(self):
        return self.__id

    @data.setter
    def data(self, data):
        self.__data = data

    @action.setter
    def action(self, action):
        self.__action = action

    @type.setter
    def type(self, type):
        self.__type = type

    @id.setter
    def id(self, id):
        self.__id = id
