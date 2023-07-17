import logging

from fastapi import APIRouter

from src.main.services import actuator_service

actuator_router = APIRouter(prefix="/actuator", tags=["Actuator"])


@actuator_router.get("/info")
async def info():
    logging.info("ACTUATOR: Info API starts processing...")
    app_info = await actuator_service.get_app_info()
    logging.info(f"ACTUATOR: Info API Response:\n{app_info}")
    return app_info
