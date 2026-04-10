from collections.abc import Iterable

import pytest

from src.utils.product_iterator import ProductIterator


def test_product_iterator_init(product_iterator: ProductIterator) -> None:
    assert isinstance(product_iterator, Iterable)
    assert product_iterator.index == 0


def test_product_iterator_iter(product_iterator: ProductIterator) -> None:
    assert product_iterator.index == 0
    next(product_iterator)
    iter(product_iterator)
    assert product_iterator.index == 0


def test_product_iterator_index_getter(product_iterator: ProductIterator) -> None:
    assert product_iterator.index == 0
    next(product_iterator)
    assert product_iterator.index == 1


def test_product_iterator(product_iterator, product) -> None:
    assert next(product_iterator) == product
    with pytest.raises(StopIteration):
        next(product_iterator)