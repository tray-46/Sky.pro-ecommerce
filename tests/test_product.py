"""test_product.py with tests for Product class"""

from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "test_product"
    assert product.description == "test_product description"
    assert product.price == 321
    assert product.quantity == 123
