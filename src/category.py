"""module with Category class definition"""

from src.product import Product
from src.utils.logger import get_logger

module_logger = get_logger(__name__)


class Category:
    """
    class to represent a category of products

    Attributes:
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

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        class constructor
        :param name: str with name of a category
        :param description: str with description of a category
        :param products: list of Products class objects associated with this category
        """
        module_logger.debug(
            f"Constructor of Category class called with: name='{name}', description='{description}', "
            f"products={", ".join([f"'{product.name}'" for product in products])}"
        )
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        module_logger.info(f"Instance of Category named '{self.name}' created")

    def add_product(self, new_product: Product) -> None:
        """
        adds new product to category
        :param new_product: Product class object
        """
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        list of products associated with category in string format
        :return: list[str], list of formatted strings describing all products in category
        """
        return "\n".join(
            [
                f"{product.name}, {product.price} руб. " f"Остаток: {product.quantity} шт."
                for product in self.__products
            ]
        )

    @property
    def products_list(self) -> list[Product]:
        """
        list of products associated with category
        :return:  list[Product], list of Product objects associated with category
        """
        return self.__products
