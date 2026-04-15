"""test_smartphone.py with tests for Smartphone class"""

import pytest

from src.smartphone import Smartphone


def test_smartphone_init(smartphone: Smartphone) -> None:
    assert smartphone.name == "test_smartphone"
    assert smartphone.description == "test_smartphone description"
    assert smartphone.price == 123456
    assert smartphone.quantity == 12
    assert smartphone.efficiency == 99.9
    assert smartphone.model == "the smartphone"
    assert smartphone.memory == 1024
    assert smartphone.color == "smartphone color"


def test_smartphone_add(smartphone: Smartphone) -> None:
    assert smartphone + smartphone == 2962944


def test_smartphone_add_error(smartphone: Smartphone) -> None:
    with pytest.raises(TypeError):
        smartphone + 1  # type: ignore


def test_smartphone_repr(smartphone: Smartphone) -> None:
    assert repr(smartphone) == ("Smartphone(name='test_smartphone', description='test_smartphone description', "
                                "price=123456, quantity=12, efficiency=99.9, model='the smartphone', memory=1024, "
                                "color='smartphone color')")
