"""module with Category class definition"""

from src.product import Product

class Category:
    """
    class to represent a category of products

    Attributes:
    categories_number: int
        class attribute: number of categories
    products_quantity: int
        class attribute: total number of products in all categories

    name: str
        name of a category
    description: str
        description of a category
    products: list[Product]
        list of products associated with this category
    """
    categories_number: int = 0
    products_quantity: int = 0


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
        Category.categories_number += 1
        Category.products_quantity += len(products)
