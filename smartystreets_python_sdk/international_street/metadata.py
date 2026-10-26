class Metadata:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/international-street-api#metadata"
        """
        self.latitude: float | None = obj.get('latitude', None)
        self.longitude: float | None = obj.get('longitude', None)
        self.geocode_precision: str | None = obj.get('geocode_precision', None)
        self.geocode_classification: str | None = obj.get('geocode_classification', None)
        self.max_geocode_precision: str | None = obj.get('max_geocode_precision', None)
        self.address_format: str | None = obj.get('address_format', None)
        self.occupant_use: str | None = obj.get("occupant_use", None)
