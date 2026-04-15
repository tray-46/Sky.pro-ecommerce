"""test_print_mixin.py with tests for PrintMixin class functionality"""

from unittest.mock import Mock, patch

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@patch("src.utils.print_mixin.repr")
def test_print_mixin(mocked_repr: Mock, capsys: pytest.CaptureFixture) -> None:
    mocked_repr.return_value = "Class(args)"
    Product("test_product", "test_product description", 321, 123)
    captured = capsys.readouterr()
    assert captured.out == "Class(args)\n"
    Smartphone(
        "test_smartphone", "test_smartphone description", 123456, 12, 99.9, "the smartphone", 1024, "smartphone color"
    )
    captured = capsys.readouterr()
    assert captured.out == "Class(args)\n"
    LawnGrass(
        "test_lawn_grass", "test_lawn_grass description", 123, 123, "test grass country", "1 day", "test grass color"
    )
    captured = capsys.readouterr()
    assert captured.out == "Class(args)\n"
