"""module with Category class definition"""

from src.product import Product
from src.utils.logger import get_logger


class Category:
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
        if not isinstance(new_product, Product):
            raise TypeError(f"Only Product and its subclasses can be added to category")
        self.__logger.debug(f"{self.__class__.__name__}.add_product called with {new_product.name}")
        self.__products.append(new_product)
        Category.product_count += 1

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
