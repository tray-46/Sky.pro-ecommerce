"""module with Category class definition"""

from src.base_products_group import BaseProductsGroup
from src.product import Product
from src.utils.exceptions import ZeroQuantityProductError
from src.utils.logger import get_logger


class Category(BaseProductsGroup):
    """
    class to represent a category of products

    Attributes:
    __logger: logging.Logger
    category_count: int
        class attribute: number of categories
    product_count: int
        class attribute: total number of products in all categories

    name: str
        name of a category
    description: str
        description of a category
    __products: list[Product]
        list of products associated with this category
    """

    __logger = get_logger(f"{__name__}.{__qualname__}")

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        class constructor
        :param name: str with name of a category
        :param description: str with description of a category
        :param products: list of Products class objects associated with this category
        """
        self.__logger.debug(
            f"Constructor of Category class called with: name='{name}', description='{description}', "
            f"products={", ".join([f"'{product.name}'" for product in products])}"
        )
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        self.__logger.info(f"Instance of Category named '{self.name}' created")

    def __str__(self) -> str:
        """Return a human-readable string representation of the category"""
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)}"

    def add_product(self, new_product: Product) -> None:
        """
        adds new product to category
        :param new_product: Product class object
        """
        self.__logger.debug(f"{self.__class__.__name__}.add_product called with {new_product}")
        if not isinstance(new_product, Product):
            self.__logger.error(
                f"TypeError: Only Product and its subclasses can be added to category, "
                f"new_product type: {type(new_product)}"
            )
            raise TypeError(
                f"Only Product and its subclasses can be added to category, new_product type: {type(new_product)}"
            )
        try:
            if new_product.quantity == 0:
                self.__logger.error("new_product's quantity cannot be zero")
                raise ZeroQuantityProductError("new_product's quantity cannot be zero")
        except ZeroQuantityProductError as e:
            print(e)
        else:
            self.__products.append(new_product)
            Category.product_count += 1
            print(f"'{new_product.name}' added to {self.name}")
            self.__logger.info(f"{new_product.name} successfully added to {self.name} product list.")
        finally:
            print("Product addition processing is complete")
            self.__logger.debug("Product addition processing is complete")

    @property
    def products(self) -> str:
        """
        list of products associated with category in string format
        :return: list[str], list of formatted strings describing all products in category
        """
        self.__logger.debug(f"Assessing '{self.name}' products")
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> list[Product]:
        """
        list of products associated with category
        :return:  list[Product], list of Product objects associated with category
        """
        self.__logger.debug(f"Assessing '{self.name}' products_list")
        return self.__products

    @products_list.setter
    def products_list(self, new_product: Product) -> None:
        if not isinstance(new_product, Product):
            self.__logger.error(f"Only 'Product' objects can be added to category: new_product is {type(new_product)}")
            raise TypeError(f"Only 'Product' objects can be added to category: new_product is {type(new_product)}")
        self.__logger.debug(f"Adding '{new_product.name}' to {self.name} products list")
        try:
            if new_product.quantity == 0:
                self.__logger.error("new_product's quantity cannot be zero")
                raise ZeroQuantityProductError("new_product's quantity cannot be zero")
        except ZeroQuantityProductError as e:
            print(e)
        else:
            self.__products.append(new_product)
            Category.product_count += 1
            print(f"'{new_product.name}' added to {self.name}")
            self.__logger.info(f"{new_product.name} added to {self.name}")
        finally:
            print("Product addition processing is complete")
            self.__logger.debug("Product addition processing is complete")

    def middle_price(self) -> float:
        """
        calculate middle price of products in category
        :return: float with middle price of products in category, if no products in category returns zero
        """
        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0.0
