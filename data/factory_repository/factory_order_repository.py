from typing import Protocol

from domain.repository import OrderRepository


class FactoryOrderRepository(Protocol):

    def provide_order_repository(self) -> OrderRepository:
        ...
