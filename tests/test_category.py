"""test_category.py with tests for Category class"""

from src.category import Category


def test_category_counters_zero():
    assert Category.category_count == 0
    assert  Category.product_count == 0


def test_category_init(category, product):
    assert category.name == "test_category"
    assert category.description == "test_category description"
    assert category.products == [product]


def test_category_counters():
    assert Category.category_count == 1
    assert Category.product_count == 1
