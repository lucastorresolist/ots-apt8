class Log:

    def __init__(self, action: str, type: str, data: str = None, id: int = None) -> None:
        self.data = data
        self.action = action
        self.type = type
        self.id = id
