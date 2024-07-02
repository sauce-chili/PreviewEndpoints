from pathlib import Path

from fastapi import APIRouter

from domain.model.request_schema import SaveApplicationRequest, SaveApplicationOfEndWeightingRequest
from domain.model.response_schema import SaveApplicationResponse, EquipmentResponse, OrderResponse
from .controller import MainControllerV1

cfg_file = Path("./configurations.yaml")

main_controller = MainControllerV1(cfg_file)

router = APIRouter()


@router.post("/save_application/", response_model=SaveApplicationResponse)
async def save_application(save_application_request: SaveApplicationRequest):
    return await main_controller.save_application(save_application_request)


@router.post("/save_application_of_end_weighting/")
async def save_application_of_end_weighting(end_weighting_request: SaveApplicationOfEndWeightingRequest):
    return await main_controller.save_application_of_end_weighting(end_weighting_request)


@router.get("/get_scales_names/")
async def get_scales_name():
    return await main_controller.get_scales_names()


@router.get("/get_equipment_list/", response_model=list[EquipmentResponse])
async def get_equipments():
    return await main_controller.get_equipments_list()


@router.get("/get_orders_list/", response_model=list[OrderResponse])
async def get_orders():
    return await main_controller.get_orders_list()
