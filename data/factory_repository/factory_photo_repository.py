from typing import Protocol

from domain.repository import PhotoRepository


class FactoryPhotoRepository(Protocol):

    def provide_photo_repository(self) -> PhotoRepository:
        ...
