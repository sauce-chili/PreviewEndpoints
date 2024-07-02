from typing import Protocol

from domain.model.entities import *


class ApplicationRepository(Protocol):

    async def save_application(self, application_form: ApplicationForm) -> ResultSaveApplication:
        ...

    async def close_application(self, closing_application_from: ClosingApplication) -> None:
        ...


class PhotoRepository(Protocol):

    async def upload_photo(self, path_to_photo: Path) -> Path:
        ...


class CameraParamsRepository(Protocol):

    async def get_cameras_param_list(self) -> list[IpCameraParam]:
        ...

    async def get_camera_param_by_name(self, name: str) -> IpCameraParam:
        ...

    async def get_camera_param_by_url(self, ip: str) -> IpCameraParam:
        ...


class ScalesParamsRepository(Protocol):

    async def get_scales_param_list(self) -> list[ScalesParam]:
        ...

    async def get_scales_param_by_name(self, name: str) -> ScalesParam:
        ...


class OrderRepository(Protocol):

    async def get_orders(self) -> list[Order]:
        ...


class EquipmentsRepository(Protocol):

    async def get_equipments(self) -> list[Equipment]:
        ...
