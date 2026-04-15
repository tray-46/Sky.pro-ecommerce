"""module with Smartphone class definition"""

from src.product import Product
from src.utils.logger import get_logger


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

    __logger = get_logger(f"{__name__}.{__qualname__}")

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
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
        self.__logger.debug(
            f"Constructor of Smartphone class called with: name='{name}', description='{description}', "
            f"price={price}, quantity: {quantity}, efficiency: {efficiency}, model: {model}, "
            f"memory: {memory}, color: {color}"
        )
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)
        self.__logger.info(f"Instance of Smartphone named '{self.name}' created")

    def __repr__(self) -> str:
        """return an unambiguous representation of the Smartphone object"""
        return (f"{self.__class__.__name__}(name='test_smartphone', description={self.description!r}, "
                f"price={self.price!r}, quantity={self.quantity!r}, "
                f"efficiency={self.efficiency!r}, model={self.model!r}, memory={self.memory!r}, color={self.color!r})")
