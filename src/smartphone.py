"""module with Smartphone class definition"""

from src.product import Product


class Smartphone(Product):
    """
        class to represent a smartphone
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

        efficiency: float
            efficiency of a smartphone
        model: str
            smartphone model name
        memory: int
            build-in memory capacity in GB
        color: str
            color of smartphone
        """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        """
        Smartphone class constructor
        :param name: str with name of a product
        :param description: str with description of a product
        :param price: float with price of a product
        :param quantity: int with quantity of a product

        :param efficiency: float with efficiency of a smartphone
        :param model: str with model name of a smartphone
        :param memory: int with memory capacity of a smartphone in GB
        :param color: str with name of smartphone color
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
