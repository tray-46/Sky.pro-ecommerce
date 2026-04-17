"""module with Product class definition"""

from typing import Optional

from src.base_product import BaseProduct
from src.utils.logger import get_logger
from src.utils.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """
    class to represent a product
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
    """

    __logger = get_logger(f"{__name__}.{__qualname__}")

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Product class constructor
        :param name: str with name of a product
        :param description: str with description of a product
        :param price: float with price of a product
        :param quantity: int with quantity of a product, must be positive number
        """
        self.__logger.debug(
            f"Constructor of Product class called with: name='{name}', description='{description}', "
            f"price={price}, quantity: {quantity}"
        )
        self.name = name
        self.description = description
        self.__price = price
        if self.varify_quantity(quantity):
            self.quantity = quantity
        super().__init__()
        self.__logger.info(f"Instance of Product named '{self.name}' created")

    def __repr__(self) -> str:
        """return an unambiguous representation of the Product object"""
        return (
            f"{self.__class__.__name__}(name={self.name!r}, description={self.description!r}, "
            f"price={self.price!r}, quantity={self.quantity!r})"
        )

    def __str__(self) -> str:
        """return a human-readable string representation of the product"""
        return f"{self.name}, {self.price} руб. " f"Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """
        add two Products objects
        :param other: Product, the other product to add
        :return: float, returns total price of both products (price1*quantity1 + price2*quantity2)
        """
        self.__logger.debug(f"'{self.name}' add '{other}'")
        if not type(other) is type(self):
            self.__logger.error(f"Can't add {type(self)} and {type(other)}")
            raise TypeError(f"Can't add {type(self)} and {type(other)}")
        result = self.__price * self.quantity + other.__price * self.quantity
        self.__logger.info(f"'{self.name}' added '{other.name}' with result: {result}")
        return result

    @classmethod
    def new_product(cls, new_product_params: dict, products_list: Optional[list[Product]] = None) -> Product:
        """
        Product class constructor
        :param new_product_params: dict with product parameters
        :param products_list: list[Product] (optional parameter), existing list of products,
                              if list contain product with new product name update existing product values
        :return: Product instance with given parameters
        """
        cls.__logger.debug(
            f"{cls.__name__} new_product called with new_product_params: {new_product_params} "
            f"and products_list: {products_list}"
        )
        # add new product to list? change product in list if updating?

        if products_list is None:
            products_list = []
        new_product_name = new_product_params.get("name", "NO_NAME")
        product = next((product for product in products_list if product.name == new_product_name), None)
        if product:
            new_product_name_price = new_product_params.get("price", 0)
            product.price = new_product_name_price if new_product_name_price > product.price else product.price
            product.quantity += new_product_params.get("quantity", 0)
            cls.__logger.info(f"new_product call update '{product.name}'")
            return product
        else:
            product = Product(**new_product_params)
            cls.__logger.info(f"new_product call create '{product.name}'")
            return product

    @property
    def price(self) -> float:
        """
        get or set price of product
        setting this will validate new price value
        if new price lower than previous ask confirmation
        :rtype: float
        """
        self.__logger.debug(f"Assessing '{self.name}' price")
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        self.__logger.debug(f"Trying to set '{self.name}' price - old value: {self.__price}, new value: {new_price}")
        if new_price > 0:
            if new_price < self.__price:
                user_input = None
                while user_input not in ["y", "n"]:
                    user_input = input(f"Do you really want to lower the price for '{self.name}'? y/n\n")
                if user_input == "y":
                    self.__logger.info(f"'{self.name}' price decreasing confirmed by user")
                    self.__price = new_price
                    self.__logger.info(f"'{self.name}' price changed to {self.__price}")
            else:
                self.__price = new_price
                self.__logger.info(f"'{self.name}' price changed to {self.__price}")
        else:
            self.__logger.error("Product price must be a positive number")
            print("Product price must be a positive number")

    @staticmethod
    def varify_quantity(quantity: int) -> bool:
        """
        varification of given quantity for product
        :param quantity: int with a quantity
        :return: bool, return True if given quantity is positive number or raises exception
        """
        if not isinstance(quantity, int):
            raise TypeError("'quantity' must be an integer")
        if quantity < 0:
            raise ValueError("'quantity' must be non negative integer")
        elif quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        return True
