class Product:

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
