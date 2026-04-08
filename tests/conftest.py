import pytest

from src.category import Category
from src.product import Product

@pytest.fixture
def product_dict() -> dict:
    return {"name": "test_product", "description": "test_product description", "price": 3210, "quantity": 123}


@pytest.fixture
def products_list() -> list[dict]:
    return [
        {"name": "test_product_1", "description": "test_product_1 description", "price": 321, "quantity": 123},
        {"name": "test_product_2", "description": "test_product_2 description", "price": 654, "quantity": 456},
    ]


@pytest.fixture
def product() -> Product:
    return Product("test_product", "test_product description", 321, 123)


@pytest.fixture
def categories_list(products_list: list[dict]) -> list[dict]:
    return [
        {"name": "category_1", "description": "category_1 description", "products": products_list},
        {"name": "category_2", "description": "category_2 description", "products": products_list},
    ]


@pytest.fixture
def category(product: Product) -> Category:
    return Category("test_category", "test_category description", [product])
