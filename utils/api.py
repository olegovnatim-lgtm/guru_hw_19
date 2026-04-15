import logging
import requests

logger = logging.getLogger(__name__)


def get(url, **kwargs):
    logger.info(f"GET {url}")
    response = requests.get(url, **kwargs)
    logger.info(f"Код ответа: {response.status_code}")
    return response