"""module with functions for data loading"""

import json
from pathlib import Path

from src.product import Product
from src.category import Category
from config import ROOT_DIR

def load_data(file_path: str) -> list[Category]:
    """
    function for loading products and categories data from JSON file
    :param file_path: str with relative path to JSON file with products and categories data
                      (path relative to root directory of the project)
    :return: list of Category objects
    """
    file_path = ROOT_DIR / file_path
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except Exception as e:
        raise e

    result = list()
    for category in data:
        products = list()
        for product in category.get("products", []):
            products.append(Product(**product))
        category["products"] = products
        result.append(Category(**category))
    return result
