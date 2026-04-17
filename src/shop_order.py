"""module with Order class definition"""

from src.base_products_group import BaseProductsGroup
from src.product import Product
from src.utils.logger import get_logger
from src.utils.exceptions import ZeroQuantityProductError


class ShopOrder(BaseProductsGroup):
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
        get or set products in order
        :return:  Product, Product objects associated with order
        """
        self.__logger.debug(f"Assessing order №'{self.order_number}' products")
        return self.__products

    @products_.setter
    def products_(self, new_product: Product) -> None:
        if not isinstance(new_product, Product):
            self.__logger.error(f"Only 'Product' objects can be added to order: new_product is {type(new_product)}")
            raise TypeError(f"Only 'Product' objects can be added to order: new_product is {type(new_product)}")
        self.__logger.debug(f"Setting order №{self.order_number} products to {new_product.name}")
        try:
            if new_product.quantity == 0:
                self.__logger.error("new_product's quantity cannot be zero")
                raise ZeroQuantityProductError("new_product's quantity cannot be zero")
        except ZeroQuantityProductError as e:
            print(e)
        else:
            self.__products = new_product
            print(f"'{new_product.name}' added to order №{self.order_number}")
            self.__logger.info(f"{new_product.name} added to order №{self.order_number}")
        finally:
            print(f"Product addition processing is complete")
            self.__logger.debug(f"Product addition processing is complete")
