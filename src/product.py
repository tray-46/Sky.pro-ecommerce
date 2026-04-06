"""module with Product class definition"""

from src.utils.logger import get_logger

module_logger = get_logger(__name__)


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
        module_logger.debug(
            f"Constructor of Product class called with: name='{name}', description='{description}', "
            f"price={price}, quantity: {quantity}"
        )
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        module_logger.info(f"Instance of Product named '{self.name}' created")
