import logging

from src.main.utils import constants


async def get_app_info():
    logging.info("Fetching Info API details...")
    return {
        "app_name": constants.APP_NAME,
        "app_code": constants.APP_CODE,
        "app_version": constants.APP_VERSION,
        "docs_url": "/docs",
        "redocs": "/redoc",
    }
