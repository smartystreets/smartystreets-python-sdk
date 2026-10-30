from .coordinate import Coordinate
from .address import Address


class Result:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#result"
        """
        self.coordinate: Coordinate = Coordinate(obj.get("coordinate", {}))
        self.distance: float | None = obj.get("distance", None)
        self.address: Address = Address(obj.get("address", {}))
