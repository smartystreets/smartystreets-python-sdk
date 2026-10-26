class Coordinate:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#coordinate"
        """
        self.latitude: float | None = obj.get('latitude', None)
        self.longitude: float | None = obj.get('longitude', None)
        self.accuracy: str | None = obj.get('accuracy', None)
        self.license: int | None = obj.get('license', None)

    def get_license(self) -> str:
        if self.license == 1:
            return "SmartyStreets Proprietary"
        else:
            return "SmartyStreets"

