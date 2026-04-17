"""test_exceptions.py with tests for custom exceptions classes"""

import pytest

from src.utils.exceptions import ZeroQuantityProductError


def test_zero_quantity_product_error() -> None:
    with pytest.raises(ZeroQuantityProductError) as err_info:
        raise ZeroQuantityProductError("Something went wrong")
    assert "Something went wrong" in str(err_info.value)
