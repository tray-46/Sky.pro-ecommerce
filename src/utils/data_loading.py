"""module with functions for data loading"""

import json
from src.utils.logger import get_logger
from src.product import Product
from src.category import Category
from config import ROOT_DIR


module_logger = get_logger(__name__)


def load_json(file_path_str: str) -> list[dict]:
    """
    function for loading data from JSON file
    :param file_path_str: str with relative path to JSON file with data
                          (path relative to root directory of the project)
    :return: list of dicts
    """
    module_logger.debug(f"Function load_json called with: file_path_str='{file_path_str}'")
    file_path = ROOT_DIR / file_path_str
    if not file_path.is_file() or file_path.stat().st_size == 0:
        module_logger.info("Specified file was not found or is empty, returning empty list")
        return []
    try:
        module_logger.debug(f"Reading file: {file_path_str}")
        with open(file_path, "r", encoding="utf-8") as json_file:
            module_logger.debug("Loading json data")
            data = json.load(json_file)
    except Exception as e:
        module_logger.error(f"Function load_transactions_data failed due to exception: {e}, returning empty list")
        return []
    if not isinstance(data, list):
        module_logger.info(f"Data read from '{file_path_str}' is not a list object, returning empty list")
        return []
    else:
        module_logger.info(f"Data read from '{file_path_str}' is successful")
        return data


def create_products(products: list[dict]) -> list[Product]:
    """
    function for creating list of Product instances
    :param products: list of dicts with product data
    :return: list of Product objects
    """
    module_logger.debug(f"Function create_products called")
    result = list()
    for product in products:
        result.append(Product(**product))
    module_logger.info(f"Function create_products completed successfully, "
                       f"returning Product objects: [{", ".join([f"'{product.name}'" for product in result])}] ")
    return result


def create_categories(categories: list[dict]) -> list[Category]:
    """
    function for creating list of Category instances
    :param categories: list of dicts with category data
    :return: list of Category objects
    """
    module_logger.debug(f"Function create_categories called")
    result = list()
    for category in categories:
        category["products"] = create_products(category.get("products", []))
        result.append(Category(**category))
    module_logger.info(f"Function create_categories completed successfully, "
                       f"returning Category objects: [{", ".join([f"'{category.name}'" for category in result])}] ")
    return result


def load_categories(file_path_str: str) -> list[Category]:
    """
    function for loading categories data from JSON file, and creating list of Category objects
    :param file_path_str:  str with relative path to JSON file with data
                          (path relative to root directory of the project)
    :return: list of Category objects
    """
    module_logger.debug(f"Function load_categories called")
    categories_data = load_json(file_path_str)
    result = create_categories(categories_data)
    module_logger.info(f"Function load_categories completed successfully, "
                       f"returning Category objects: [{", ".join([f"'{category.name}'" for category in result])}] ")
    return result

