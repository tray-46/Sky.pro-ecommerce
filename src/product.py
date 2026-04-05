"""module with Product class definition"""

class Product:
    """
    class to represent a product

    Attributes:
    name: str
        name of a product
    description: str
        description of a product
    price: float
        price of a product
    quantity: int
        quantity of a product
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Person class constructor
        :param name: str with name of a product
        :param description: str with description of a product
        :param price: float with price of a product
        :param quantity: int with quantity of a product
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
