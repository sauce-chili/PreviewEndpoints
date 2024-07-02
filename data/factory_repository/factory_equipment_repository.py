from typing import Protocol

from domain.repository import EquipmentsRepository


class FactoryEquipmentsRepository(Protocol):

    def provide_equipments_repository(self) -> EquipmentsRepository:
        ...
