from typing import Protocol

from domain.repository import ApplicationRepository


class FactoryApplicationsRepository(Protocol):

    def provide_application_repository(self) -> ApplicationRepository:
        ...
