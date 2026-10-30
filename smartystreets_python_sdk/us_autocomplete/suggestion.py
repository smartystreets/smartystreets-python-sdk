from typing import Any


class Suggestion:
    def __init__(self, obj: Any = None) -> None:
        """
        See "https://www.smarty.com/docs/apis/us-autocomplete-v2/reference#http-response-status"
        """
        self.smarty_key: str | None = obj.get('smarty_key', None)
        self.entry_id: str | None = obj.get('entry_id', None)
        self.urbanization: str | None = obj.get('urbanization', None)
        self.street_line: str | None = obj.get('street_line', None)
        self.secondary: str | None = obj.get('secondary', None)
        self.city: str | None = obj.get('city', None)
        self.state: str | None = obj.get('state', None)
        self.zipcode: str | None = obj.get('zipcode', None)
        self.entries: int | None = obj.get('entries', None)
        self.source: str | None = obj.get('source', None)
