from fastapi import APIRouter

from src.main.routers import actuator_router

app_router = APIRouter()


## Mapping Actuator Routers
app_router.include_router(actuator_router.actuator_router)
