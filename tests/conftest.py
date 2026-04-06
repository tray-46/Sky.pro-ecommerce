import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def product() -> Product:
    return Product("test_product", "test_product description", 321, 123)


@pytest.fixture
def category(product) -> Category:
    return Category("test_category", "test_category description", [product])
