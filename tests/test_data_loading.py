"""test_data_loading.py with tests for data_loading.py module functions"""

import json
from unittest.mock import Mock, patch

from src.category import Category
from src.product import Product
from src.utils.data_loading import create_categories, create_products, load_categories, load_json

JSON_FILE_PATH = "data/products.json"


def test_load_json_bad_file() -> None:
    assert load_json("non_existing_file.json") == []
    mock_stat_result = Mock(st_size=0)
    with patch("pathlib.Path.stat", return_value=mock_stat_result):
        assert load_json(JSON_FILE_PATH) == []


@patch("json.load")
def test_load_json(mock_load: Mock) -> None:
    mock_load.return_value = 1
    assert load_json(JSON_FILE_PATH) == []
    mock_load.return_value = []
    assert load_json(JSON_FILE_PATH) == []
    mock_load.return_value = [
        {
            "name": "name",
        }
    ]
    assert load_json(JSON_FILE_PATH) == [
        {
            "name": "name",
        }
    ]


@patch("src.utils.data_loading.json.load")
def test_load_json_json_error(mock_load: Mock) -> None:
    mock_load.side_effect = json.JSONDecodeError("Invalid JSON", "1", 0)
    assert load_json(JSON_FILE_PATH) == []
    mock_load.assert_called_once()


def test_create_products(products_list: list[dict]) -> None:
    result = create_products(products_list)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(product, Product) for product in result)


def test_create_categories(categories_list: list[dict]) -> None:
    result = create_categories(categories_list)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(category, Category) for category in result)
    assert all(isinstance(product, Product) for product in result[0].products_list)


@patch("src.utils.data_loading.create_categories")
@patch("src.utils.data_loading.load_json")
def test_load_categories(
    mocked_load_json: Mock, mocked_create_categories: Mock, categories_list: list[dict], category: Category
) -> None:
    mocked_load_json.return_value = categories_list
    mocked_create_categories.return_value = [category]
    result = load_categories(JSON_FILE_PATH)
    assert isinstance(result, list)
    assert len(result) == 1
    assert all(isinstance(category, Category) for category in result)
    assert all(isinstance(product, Product) for product in result[0].products_list)
