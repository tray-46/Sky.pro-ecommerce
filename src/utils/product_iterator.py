"""module with ProductIterator class definition"""

from src.category import Category
from src.utils.logger import get_logger


class ProductIterator:
    """
    Support class for iterating products in given category

    Attributes:
    __logger: logging.Logger

    __products_list: list[Product]
        list of Product objects to iterate through
    __index: int
        current index of product

    """
    __logger = get_logger(f"{__name__}.{__qualname__}")

    def __init__(self, product_category: Category) -> None:
        """
        class constructor
        :param product_category: Category object
        """
        self.__logger.debug("Constructor of Product class called")
        self.__products_list = product_category.products_list
        self.__index = 0
        self.__logger.info(f"Instance of ProductIterator created")

    def __iter__(self) -> ProductIterator:
        """Return an iterator over the products list"""
        self.__index = 0
        self.__logger.debug(f"Returning ProductIterator, index set to 0")
        return self

    def __next__(self):
        """Return the next product from the list or raise StopIteration"""
        self.__logger.debug(f"ProductIterator called")
        if self.__index < len(self.__products_list):
            product = self.__products_list[self.__index]
            self.__logger.info(f"Returning Product {product.name}, index: {self.__index}")
            self.__index += 1
            return product
        else:
            self.__logger.info(f"ProductIterator reached the end of the list")
            raise StopIteration

    @property
    def index(self) -> int:
        """Return the current index of the product"""
        self.__logger.debug(f"Assessing ProductIterator index")
        return self.__index
