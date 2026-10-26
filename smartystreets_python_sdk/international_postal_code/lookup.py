from smartystreets_python_sdk.international_postal_code.candidate import Candidate
from typing import Any


class Lookup:
    def __init__(self) -> None:
        """
        In addition to holding all the input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/international-postal-code-api"
        """
        self.results: list[Candidate] = []
        
        self.input_id: str | None = None
        self.country: str | None = None
        self.locality: str | None = None
        self.administrative_area: str | None = None
        self.postal_code: str | None = None

    def populate(self, params: dict[str, Any]) -> None:
        if self.input_id:
            params['input_id'] = self.input_id
        if self.country:
            params['country'] = self.country
        if self.locality:
            params['locality'] = self.locality
        if self.administrative_area:
            params['administrative_area'] = self.administrative_area
        if self.postal_code:
            params['postal_code'] = self.postal_code
