from typing import Protocol

from domain.model.entities import *


class CameraController(Protocol):

    async def take_photo(self, output_file_name: str, camera: IpCameraParam) -> Path:
        ...


class WeightCalculator(Protocol):

    def calculate(self, gross_w, container_w, extra_w) -> CalculatedWeights:
        ...


class ScaleController(Protocol):

    async def weight(self, scales: ScalesParam) -> WeighingResult:
        ...
