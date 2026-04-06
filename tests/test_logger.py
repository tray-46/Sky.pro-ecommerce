import logging

import pytest

from src.utils.logger import get_logger


def test_get_logger_base(caplog: pytest.LogCaptureFixture) -> None:
    logger = get_logger(__name__)
    assert isinstance(logger, logging.Logger)
    assert logger.name == __name__

    logger.info("Info message")
    caplog.set_level(logging.INFO)

    assert len(caplog.records) >= 1
    record = caplog.records[0]
    assert record.levelname == "INFO"
    assert record.message == "Info message"
    assert record.name == __name__

    logger.error("Error message")
    caplog.set_level(logging.WARNING)

    assert "Error message" in caplog.text
    assert caplog.records[1].levelname == "ERROR"


def test_get_logger_error(caplog: pytest.LogCaptureFixture) -> None:
    logger = get_logger(__name__)
    logger.error("Error message")
    caplog.set_level(logging.WARNING)

    assert "Error message" in caplog.text
    assert caplog.records[0].levelname == "ERROR"
