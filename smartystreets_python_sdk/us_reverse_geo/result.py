from .coordinate import Coordinate
from .address import Address


class Result:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#result"
        """
        self.coordinate = Coordinate(obj.get("coordinate", {}))
        self.distance = obj.get("distance", None)
        self.address = Address(obj.get("address", {}))
