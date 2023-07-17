import logging

import coloredlogs
from fastapi import FastAPI

from src.main.routers import routes_mapper
from src.main.utils import constants

# Make sure to define the logger object
logger = logging.getLogger(__name__)
coloredlogs.install(
    level="INFO", fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title=constants.APP_NAME,
    description=constants.APP_DESC,
    version="0.0.1",
    contact={"name": "Shaik Malik Basha", "email": "shaikmalikbasha@example.com"},
    license_info={"name": "MIT"},
)


@app.get("/")
async def index():
    logging.info("Index API triggered...")
    res = {"docs_url": "/docs", "redocs": "/redoc"}
    logging.info(f"Index API Response: {res}")
    return res


app.include_router(routes_mapper.app_router, prefix=constants.API_VERSION)
