from smartystreets_python_sdk.international_postal_code.language_mode import LanguageMode
from smartystreets_python_sdk.max_results import normalize_max_results
from smartystreets_python_sdk.international_postal_code.candidate import Candidate
from typing import Any


class Lookup:
    def __init__(self) -> None:
        """
        In addition to holding all the input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.

        See "https://smartystreets.com/docs/cloud/international-postal-code-api"

        :field self.language: When not set, results are returned using the Latin character set.
            When set to LanguageMode.NATIVE (JPN only), results are returned in the native character set for that country.
            When set to LanguageMode.LATIN, results use the Latin character set with accents and other diacritics removed.
        :field self.max_results: The maximum number of results to return. Sent only when greater than 0.
        """
        self.results: list[Candidate] = []

        self.input_id: str | None = None
        self.country: str | None = None
        self.language: str | None = None
        self.locality: str | None = None
        self.administrative_area: str | None = None
        self.postal_code: str | None = None
        self.max_results: str | None = None

    def populate(self, params: dict[str, Any]) -> None:
        if self.input_id:
            params['input_id'] = self.input_id
        if self.country:
            params['country'] = self.country
        if self.language is not None:
            params['language'] = LanguageMode.from_value(self.language).value
        if self.locality:
            params['locality'] = self.locality
        if self.administrative_area:
            params['administrative_area'] = self.administrative_area
        if self.postal_code:
            params['postal_code'] = self.postal_code
        max_results = normalize_max_results(self.max_results)
        if max_results is not None:
            params['max_results'] = max_results
