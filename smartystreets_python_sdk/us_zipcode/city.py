class City:
    def __init__(self, obj: dict) -> None:
        """
        Known in the SmartyStreets US ZIP Code API documentation as a city_state
        See "https://smartystreets.com/docs/cloud/us-zipcode-api#cities"
        """
        self.city: str | None = obj.get('city')
        self.mailable_city: bool | None = obj.get('mailable_city')
        self.state_abbreviation: str | None = obj.get('state_abbreviation')
        self.state: str | None = obj.get('state')
