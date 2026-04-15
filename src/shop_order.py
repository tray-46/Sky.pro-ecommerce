"""module with Order class definition"""

from src.product import Product
from src.utils.logger import get_logger


class ShopOrder:
    """
    class to represent a shop order

    Attributes:
    __logger: logging.Logger
    ID: int
        class attribute: id for next order

    order_number: int
        id of an order
    __products: Product
        link to ordered products (ссылка в смысле ссылка на объект или url ???)

    quantity: int
        quantity of ordered products
    total_cost: float
        total cost of ordered products
    """

    __logger = get_logger(f"{__name__}.{__qualname__}")

    ID = 1

    def __init__(self, products: Product, quantity: int) -> None:
        """
        class constructor
        :param products: Product class object, link to ordered products
        :param quantity: int, quantity of ordered products
        """
        self.__logger.debug(
            f"Constructor of ShopOrder class called with: products={products.name}, quantity={quantity}"
        )
        self.order_number = self.__class__.ID
        self.__class__.ID += 1
        self.__products = products
        self.quantity = quantity
        self.total_cost = self.__products.price * self.quantity
        self.__logger.info(f"Instance of ShopOrder number '{self.order_number}' created")

    def __str__(self) -> str:
        """Return a human-readable string representation of the order"""
        return (
            f"Заказ №{self.order_number}: {self.__products.name} в количестве {self.quantity} шт., "
            f"общая стоимость: {self.total_cost} ₽"
        )

    @property
    def products(self) -> str:
        """
        ordered product in string format
        :return: str, formatted strings describing ordered product
        """
        self.__logger.debug(f"Assessing order №'{self.order_number}' products")
        return str(self.__products)

    @property
    def products_(self) -> Product:
        """
        list of products associated with category
        :return:  list[Product], list of Product objects associated with category
        """
        self.__logger.debug(f"Assessing order №'{self.order_number}' products")
        return self.__products
