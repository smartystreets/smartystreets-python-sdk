from .coordinate import Coordinate
from .address import Address


class Result:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#result"
        """
        for result in obj:
            self.coordinate = Coordinate(result.get("coordinate", {}))
            self.distance = result.get("distance", None)
            self.address = Address(result.get("address", {}))
