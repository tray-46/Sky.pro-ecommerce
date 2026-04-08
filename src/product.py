"""module with Product class definition"""

from typing import Optional

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
    __price: float
        price of a product
    quantity: int
        quantity of a product
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Product class constructor
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
        self.__price = price
        self.quantity = quantity
        module_logger.info(f"Instance of Product named '{self.name}' created")

    @classmethod
    def new_product(cls, new_product_params: dict, products_list: Optional[list[Product]] = None) -> Product:
        """
        Product class constructor
        :param new_product_params: dict with product parameters
        :param products_list: list[Product] (optional parameter), existing list of products,
                              if list contain product with new product name update existing product values
        :return: Product instance with given parameters
        """

        # add new product to list? change product in list if updating?

        if products_list is None:
            products_list = []
        new_product_name = new_product_params.get("name", "NO_NAME")
        product = next((product for product in products_list if product.name == new_product_name), None)
        if product:
            new_product_name_price = new_product_params.get("price", 0)
            product.price = new_product_name_price if new_product_name_price > product.price else product.price
            product.quantity += new_product_params.get("quantity", 0)
            return product
        else:
            return Product(**new_product_params)


    @property
    def price(self) -> float:
        """
        get or set price of product
        setting this will validate new price value
        if new price lower than previous ask confirmation
        :rtype: float
        """
        return self.__price


    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            if new_price < self.__price:
                user_input = None
                while user_input not in ["y", "n"]:
                    user_input = input(f"Do you really want to lower the price for '{self.name}'? y/n\n")
                if user_input == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Product price must be a positive number")
