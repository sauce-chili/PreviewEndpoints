from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass
class SaveApplicationResponse(BaseModel):
    weight_gross: float
    weight_net: float
    url_photo: str


@dataclass
class ScalesTypeResponse(BaseModel):
    nameEng: str
    nameRu: str


@dataclass
class OrderResponse(BaseModel):
    counterparty: str
    car_plates: list[str]


@dataclass
class EquipmentResponse(BaseModel):
    name: str
