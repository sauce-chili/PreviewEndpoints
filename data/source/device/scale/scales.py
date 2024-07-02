from typing import Protocol
from decimal import Decimal


class Scales(Protocol):

    def weigh(self) -> Decimal:
        ...
