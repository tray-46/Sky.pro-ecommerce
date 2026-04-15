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


@pytest.mark.parametrize(
    "product1, product2",
    [
        ("product", "smartphone"),
        ("product", "lawn_grass"),
        ("smartphone", "product"),
        ("smartphone", "lawn_grass"),
        ("lawn_grass", "product"),
        ("lawn_grass", "smartphone"),
    ],
)
def test_task_add_error(product1: str, product2: str, request: pytest.FixtureRequest, product: Product) -> None:
    product1 = request.getfixturevalue(product1)
    product2 = request.getfixturevalue(product2)
    with pytest.raises(TypeError):
        product1 + product2
    with pytest.raises(TypeError):
        product + 1  # type: ignore


def test_product_repr(product: Product) -> None:
    assert repr(product) == (
        "Product(name='test_product', description='test_product description', price=321, " "quantity=123)"
    )
