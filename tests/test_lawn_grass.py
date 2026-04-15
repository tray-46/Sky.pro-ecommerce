"""test_lawn_grass.py with tests for LawnGrass class"""

import pytest

from src.lawn_grass import LawnGrass


def test_lawn_grass_init(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.name == "test_lawn_grass"
    assert lawn_grass.description == "test_lawn_grass description"
    assert lawn_grass.price == 123
    assert lawn_grass.quantity == 123
    assert lawn_grass.country == "test grass country"
    assert lawn_grass.germination_period == "1 day"
    assert lawn_grass.color == "test grass color"


def test_lawn_grass_add(lawn_grass: LawnGrass) -> None:
    assert lawn_grass + lawn_grass == 30258


def test_lawn_grass_add_error(lawn_grass: LawnGrass) -> None:
    with pytest.raises(TypeError):
        lawn_grass + 1  # type: ignore


def test_lawn_grass_repr(lawn_grass: LawnGrass) -> None:
    assert repr(lawn_grass) == ("LawnGrass(name='test_lawn_grass', description='test_lawn_grass description', "
                                "price=123, quantity=123, country='test grass country', "
                                "germination_period='1 day', color='test grass color')")
