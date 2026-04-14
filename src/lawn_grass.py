"""module with LawnGrass class definition"""

from product import Product


class LawnGrass(Product):
    """
    class to represent a lawn grass
    __logger: logging.Logger

    Attributes:
    name: str
        name of a product
    description: str
        description of a product
    __price: float
        price of a product
    quantity: int
        quantity of a product

    country: str
        lawn grass's country of origin
    germination_period: str
        germination period of lawn grass
    color: str
        color of lawn grass
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str) -> None:
        """
        LawnGrass class constructor
        :param name: str with name of a product
        :param description: str with description of a product
        :param price: float with price of a product
        :param quantity: int with quantity of a product

        :param country: str with lawn grass's country of origin
        :param germination_period: str with germination period of lawn grass
        :param color: str with color of lawn grass
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
