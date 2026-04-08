"""module with logging functions"""

import logging

from config import ROOT_DIR


def get_logger(logger_name: str) -> logging.Logger:
    """
    function for creating and setting up logger
    :param logger_name: str with name of logger
    :return: logging.Logger object
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    log_file_path = ROOT_DIR / "logs" / f"{logger_name}.log"
    file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger
