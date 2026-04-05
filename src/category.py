"""module with Category class definition"""

from src.product import Product

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
    products: list[Product]
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
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
