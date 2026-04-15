"""module with LawnGrass class definition"""

from src.product import Product

from src.utils.logger import get_logger


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

    __logger = get_logger(f"{__name__}.{__qualname__}")

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
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
        self.__logger.debug(
            f"Constructor of Smartphone class called with: name='{name}', description='{description}', "
            f"price={price}, quantity: {quantity}, country: {country}, "
            f"germination_period : {germination_period}, color: {color}"
        )
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
        self.__logger.info(f"Instance of LawnGrass named '{self.name}' created")

    def __repr__(self) -> str:
        """return an unambiguous representation of the LawnGrass object"""
        return (f"{self.__class__.__name__}(name={self.name!r}, description={self.description!r}, "
                f"price={self.price!r}, quantity={self.quantity!r}, "
                f"country={self.country!r}, germination_period={self.germination_period!r}, color={self.color!r})")
