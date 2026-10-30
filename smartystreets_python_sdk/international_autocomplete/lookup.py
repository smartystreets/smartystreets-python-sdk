from smartystreets_python_sdk.international_autocomplete.candidate import Candidate
from smartystreets_python_sdk.international_autocomplete.language_mode import LanguageMode
from typing import Any


class Lookup:
    def __init__(self, search: str | None = None, address_id: str | None = None, country: str | None = None,
                 max_results: int = 5, max_group_results: int = 100, geolocation: bool = False,
                 locality: str | None = None, postal_code: str | None = None,
                 language: LanguageMode | str | None = None) -> None:
        """
        In addition to holding all the input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.

        :param country: The country where the desired address is located (required)
        :param search: The part of the address tht has already been typed (required)
        :param administrative_area: Limit the results to only the administrative area provided
        :param locality: Limit the results to only the locality provided
        :param postal_code: Limit the results to only the postal code provided
        :param language: The output language, Native or Latin (defaults to the country's language)
        """
        self.result: list[Candidate] = []

        self.custom_parameter_array: dict[str, Any] = {}
        self.search = search
        self.address_id = address_id
        self.country = country
        self.max_results = max_results
        self.max_group_results = max_group_results
        self.geolocation = geolocation
        self.locality = locality
        self.postal_code = postal_code
        self.language = language

    def add_custom_parameter(self, parameter: str, value: Any) -> None:
        self.custom_parameter_array[parameter] = value
