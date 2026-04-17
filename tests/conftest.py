import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.shop_order import ShopOrder
from src.smartphone import Smartphone
from src.utils.product_iterator import ProductIterator


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
def smartphone() -> Smartphone:
    return Smartphone(
        "test_smartphone", "test_smartphone description", 123456, 12, 99.9, "the smartphone", 1024, "smartphone color"
    )


@pytest.fixture
def lawn_grass() -> LawnGrass:
    return LawnGrass(
        "test_lawn_grass", "test_lawn_grass description", 123, 123, "test grass country", "1 day", "test grass color"
    )


@pytest.fixture
def categories_list(products_list: list[dict]) -> list[dict]:
    return [
        {"name": "category_1", "description": "category_1 description", "products": products_list},
        {"name": "category_2", "description": "category_2 description", "products": products_list},
    ]


@pytest.fixture
def category(product: Product) -> Category:
    return Category("test_category", "test_category description", [product])

@pytest.fixture
def category_no_products() -> Category:
    return Category("test_category", "test_category description", [])


@pytest.fixture
def product_iterator(category: Category) -> ProductIterator:
    return ProductIterator(category)


@pytest.fixture
def shop_order(product: Product) -> ShopOrder:
    return ShopOrder(product, 1)
