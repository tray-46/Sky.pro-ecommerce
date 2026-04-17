"""test_category.py with tests for Category class"""

import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


def test_category_products_list_setter(category: Category, product: Product, capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(TypeError):
        category.products_list = 1  # type: ignore
    assert len(category.products_list) == 1
    category.products_list = product
    captured = capsys.readouterr()
    assert captured.out == "'test_product' added to test_category\nProduct addition processing is complete\n"
    assert len(category.products_list) == 2
    assert category.products_list[1] == product
    product.quantity = 0
    category.products_list = product
    captured = capsys.readouterr()
    assert captured.out == "new_product's quantity cannot be zero\nProduct addition processing is complete\n"
    assert len(category.products_list) == 2


def test_category_products_getter(category: Category) -> None:
    assert category.products == "test_product, 321 руб. Остаток: 123 шт."


def test_category_add_product(
    category: Category, product: Product, smartphone: Smartphone, lawn_grass: LawnGrass, capsys: pytest.CaptureFixture
) -> None:
    assert len(category.products_list) == 1
    category.add_product(product)
    assert len(category.products_list) == 2
    category.add_product(smartphone)
    assert len(category.products_list) == 3
    category.add_product(lawn_grass)
    assert len(category.products_list) == 4
    with pytest.raises(TypeError):
        category.add_product(1)  # type: ignore
    assert len(category.products_list) == 4
    capsys.readouterr()
    product.quantity = 0
    category.add_product(product)
    captured = capsys.readouterr()
    assert captured.out == "new_product's quantity cannot be zero\nProduct addition processing is complete\n"
    assert len(category.products_list) == 4


def test_category_str(category: Category) -> None:
    assert str(category) == "test_category, количество продуктов: 123"


def test_category_middle_price(category: Category, category_no_products: Category) -> None:
    assert category.middle_price() == 321.0
    assert category_no_products.middle_price() == 0.0
