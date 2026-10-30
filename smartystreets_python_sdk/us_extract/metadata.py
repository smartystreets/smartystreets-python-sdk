class Metadata:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-extract-api#http-response-status"
        """
        self.lines: int | None = obj.get('lines', None)
        self.unicode: bool | None = obj.get('unicode', None)
        self.address_count: int | None = obj.get('address_count', None)
        self.verified_count: int | None = obj.get('verified_count', None)
        self.bytes: int | None = obj.get('bytes', None)
        self.character_count: int | None = obj.get('character_count', None)
