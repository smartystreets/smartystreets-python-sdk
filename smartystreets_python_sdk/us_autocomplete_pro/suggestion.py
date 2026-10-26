from typing import Any


class Suggestion:
    def __init__(self, obj: Any = None) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-autocomplete-api#http-response"
        """
        self.street_line: str | None = obj.get('street_line', None)
        self.secondary: str | None = obj.get('secondary', None)
        self.city: str | None = obj.get('city', None)
        self.state: str | None = obj.get('state', None)
        self.zipcode: str | None = obj.get('zipcode', None)
        self.entries: int | None = obj.get('entries', None)
