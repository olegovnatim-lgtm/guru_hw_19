import logging
import pytest
from config import BASE_URL


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )


@pytest.fixture
def base_url():
    return BASE_URL