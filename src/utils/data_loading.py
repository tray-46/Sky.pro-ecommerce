"""module with functions for data loading"""

import json
from src.utils.logger import get_logger
from src.product import Product
from src.category import Category
from config import ROOT_DIR


module_logger = get_logger(__name__)


def load_data(file_path_str: str) -> list[Category]:
    """
    function for loading products and categories data from JSON file
    :param file_path_str: str with relative path to JSON file with products and categories data
                      (path relative to root directory of the project)
    :return: list of Category objects
    """
    file_path = ROOT_DIR / file_path_str
    if not file_path.is_file() or file_path.stat().st_size == 0:
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(e)
        return []
    result = list()
    try:
        for category in data:
            products = list()
            for product in category.get("products", []):
                products.append(Product(**product))
            category["products"] = products
            result.append(Category(**category))
        return result
    except Exception as e:
        print(e)
        return []
