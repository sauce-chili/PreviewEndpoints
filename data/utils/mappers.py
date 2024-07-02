from data.model.dto import ApplicationStorageDto, EquipmentStorageDto, OrderStorageDto
from domain.model.entities import ClosingApplication, ApplicationForm, Equipment, Order

__TIME_FORMAT: str = "%d-%m-%Y-%H-%M-%S"


def ClosingApplication_to_ApplicationStorageDto(id: str, form: ClosingApplication) -> ApplicationStorageDto:
    return ApplicationStorageDto(
        id=id,
        car_plate=form.car_plate,
        counterparty=form.counterparty,
        operation_type=form.operation_type,
        equipment_type=form.equipment_type,
        camera_type=None,
        scales_type=None,
        weight_gross=None,
        weight_extra=None,
        weight_net=None,
        weight_container=None,
        url_photo=None,
        date=form.date.strftime(__TIME_FORMAT),
        end_weighing=True
    )


def ApplicationStorageDto_to_ApplicationStorageDto(
        app_form: ApplicationForm,
        id: str,
        ftp_url_photo: str = None
) -> ApplicationStorageDto:
    return ApplicationStorageDto(
        id=id,
        counterparty=app_form.counterparty,
        car_plate=app_form.car_plate,
        operation_type=app_form.operation_type,
        equipment_type=app_form.equipment_type,
        camera_type=app_form.camera_type,
        scales_type=app_form.scales_type,
        weight_gross=str(app_form.weight_gross),
        weight_extra=str(app_form.weight_extra),
        weight_container=str(app_form.weight_container),
        weight_net=str(app_form.weight_net),
        url_photo=ftp_url_photo,
        date=app_form.date.strftime(__TIME_FORMAT),
        end_weighing=False
    )


def EquipmentStorageDto_to_Equipment(dto: EquipmentStorageDto) -> Equipment:
    return Equipment(name=dto.name)
