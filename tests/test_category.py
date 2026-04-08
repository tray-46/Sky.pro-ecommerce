"""test_category.py with tests for Category class"""

from src.category import Category
from src.product import Product


def test_category_counters_zero() -> None:
    assert Category.category_count == 0
    assert Category.product_count == 0


def test_category_init(category: Category, product: Product) -> None:
    assert category.name == "test_category"
    assert category.description == "test_category description"
    assert category.products_list == [product]


def test_category_counters() -> None:
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_products_list_getter(category: Category, product: Product) -> None:
    assert category.products_list == [product]


def test_category_products_getter(category: Category) -> None:
    assert category.products == 'test_product, 321 руб. Остаток: 123 шт.'


def test_category_add_product(category: Category, product: Product) -> None:
    assert len(category.products_list) == 1
    category.add_product(product)
    assert len(category.products_list) == 2
