from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from pathlib import Path


@dataclass(frozen=True)
class PreservationApplicationForm:
    """
    A class that stores the data necessary to save application form
    """
    car_plate: str
    counterparty: str
    operation_type: str
    equipment_type: str
    camera_type: str | None
    scales_type: str
    weight_extra: float
    weight_container: float


@dataclass(frozen=True)
class ClosingApplication:
    car_plate: str
    counterparty: str
    equipment_type: str
    operation_type: str
    date: datetime


@dataclass(frozen=True)
class ApplicationForm:
    car_plate: str
    counterparty: str
    operation_type: str
    equipment_type: str | None
    camera_type: str | None
    scales_type: str | None
    weight_gross: float | None
    weight_extra: float | None
    weight_container: float | None
    weight_net: float | None
    local_path_photo: Path | None
    date: datetime


@dataclass(frozen=True)
class ResultSaveApplication:
    url_photo: str
    weight_gross: float
    weight_net: float


@dataclass(frozen=True)
class Order:
    counterparty: str
    car_plates: list[str]


@dataclass(frozen=True)
class Equipment:
    name: str


@dataclass(frozen=True)
class IpCameraParam:
    url: str
    name: str


@dataclass(frozen=True)
class ScalesParam:
    nameOrigin: str
    nameRu: str
    port: str


@dataclass(frozen=True)
class WeighingResult:
    result: Decimal


@dataclass(frozen=True)
class CalculatedWeights:
    weight_gross: Decimal
    weight_net: Decimal
