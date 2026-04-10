"""test_product.py with tests for Product class"""

import pytest

from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "test_product"
    assert product.description == "test_product description"
    assert product.price == 321
    assert product.quantity == 123


def test_product_new_product(product_dict: dict) -> None:
    new_product = Product.new_product(product_dict)
    assert new_product.name == "test_product"
    assert new_product.description == "test_product description"
    assert new_product.price == 3210
    assert new_product.quantity == 123


def test_product_new_product_with_list(product_dict: dict, product: Product) -> None:
    new_product = Product.new_product(product_dict, [product])
    assert new_product.name == "test_product"
    assert new_product.description == "test_product description"
    assert new_product.price == 3210
    assert new_product.quantity == 246


def test_product_price_getter(product: Product) -> None:
    assert product.price == 321


def test_product_price_setter(
    product: Product, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    inputs = iter(["n", "some_nonsense", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    product.price = 3210
    assert product.price == 3210
    product.price = 123
    assert product.price == 3210
    product.price = 123
    assert product.price == 123
    product.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Product price must be a positive number\n"
    product.price = -1
    captured = capsys.readouterr()
    assert captured.out == "Product price must be a positive number\n"


def test_product_str(product: Product) -> None:
    assert str(product) == "test_product, 321 руб. Остаток: 123 шт."


def test_product_add(product: Product) -> None:
    assert product + product == 78966