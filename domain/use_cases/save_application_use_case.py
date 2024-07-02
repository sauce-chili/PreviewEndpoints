from domain.device_controller import CameraController, ScaleController, WeightCalculator
from domain.repository import (
    ApplicationRepository,
    CameraParamsRepository,
    ScalesParamsRepository,
)


class SaveApplicationUseCase:

    def __init__(
            self,
            application_repository: ApplicationRepository,
            cameras_repository: CameraParamsRepository,
            scales_repository: ScalesParamsRepository,
            ip_cam_controller: CameraController,
            scales_controller: ScaleController,
            weight_calculator: WeightCalculator,
    ):
        self.__application_rep = application_repository
        self.__cam_rep = cameras_repository
        self.__scales_rep = scales_repository
        self.__ip_cam_controller = ip_cam_controller
        self.__scales_controller = scales_controller
        self.__weight_calculator = weight_calculator



    ...
