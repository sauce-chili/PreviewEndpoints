from typing import Protocol

from numpy import ndarray


class Camera(Protocol):
    def take_photo(self) -> ndarray:
        ...
