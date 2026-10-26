class Address:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#address"
        """
        self.street: str | None = obj.get('street', None)
        self.city: str | None = obj.get('city', None)
        self.state_abbreviation: str | None = obj.get('state_abbreviation', None)
        self.zipcode: str | None = obj.get('zipcode', None)
        self.source: str | None = obj.get('source', None)
        self.smartykey: str | None = obj.get('smarty_key', None)
