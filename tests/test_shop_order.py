"""test_shop_order.py with tests for ShopOrder class"""

import pytest

from src.product import Product
from src.shop_order import ShopOrder


def test_shop_order_start_id() -> None:
    assert ShopOrder.ID == 1


def test_shop_order_init(shop_order: ShopOrder, product: Product) -> None:
    assert shop_order.order_number == 1
    assert shop_order.products_ == product
    assert shop_order.quantity == 1
    assert shop_order.total_cost == 321
    assert ShopOrder.ID == 2


def test_shop_order_products_getter(shop_order: ShopOrder, product: Product) -> None:
    assert shop_order.products_ == product


def test_shop_order_products_setter(shop_order: ShopOrder, product: Product, capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(TypeError):
        shop_order.products_ = 1  # type: ignore
    shop_order.products_ = product
    captured = capsys.readouterr()
    assert captured.out == "'test_product' added to order №3\nProduct addition processing is complete\n"
    product.quantity = 0
    shop_order.products_ = product
    captured = capsys.readouterr()
    assert captured.out == "new_product's quantity cannot be zero\nProduct addition processing is complete\n"


def test_shop_order_products_str_getter(shop_order: ShopOrder) -> None:
    assert shop_order.products == "test_product, 321 руб. Остаток: 123 шт."


def test_shop_order_str(shop_order: ShopOrder) -> None:
    assert str(shop_order) == "Заказ №5: test_product в количестве 1 шт., общая стоимость: 321 ₽"
