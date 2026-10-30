from smartystreets_python_sdk.exceptions import UnprocessableEntityError
from smartystreets_python_sdk.international_street.language_mode import LanguageMode
from smartystreets_python_sdk.international_street.candidate import Candidate
from typing import Any


class Lookup:
    def __init__(self, freeform: str | None = None, country: str | None = None) -> None:
        """
        In addition to holding all of the input data for this lookup, this class also will contain the 
        result of the lookup after it comes back from the API.
        
        Note: Lookups must have certain required fields set with non-blank values.
            These can be found at the URL below.
            
        See "https://smartystreets.com/docs/cloud/international-street-api#http-input-fields"
        
        :field self.geocode: Disabled by default. Set to true to enable.
        :field self.language: When not set, the output language will match the language of the input values.
            When set to language_mode.NATIVE, the results will always be in the language of the output country.
            When set to language_mode.LATIN, the results will always be provided using a Latin character set.
        :field self.max_results: The maximum number of candidates to return. Sent only when greater than 0.
        """
        self.result: list[Candidate] = []

        self.custom_parameter_array: dict[str, Any] = {}
        self.input_id: str | None = None
        self.country: str | None = country
        self.geocode: bool | str | None = None
        self.language: LanguageMode | str | None = None
        self.freeform: str | None = freeform
        self.address1: str | None = None
        self.address2: str | None = None
        self.address3: str | None = None
        self.address4: str | None = None
        self.organization: str | None = None
        self.locality: str | None = None
        self.administrative_area: str | None = None
        self.postal_code: str | None = None
        self.features: str | None = None
        self.max_results: str | None = None

    @property
    def missing_country(self) -> bool:
        return self.field_is_missing(self.country)

    @property
    def has_freeform(self) -> bool:
        return self.field_is_set(self.freeform)

    @property
    def missing_address1(self) -> bool:
        return self.field_is_missing(self.address1)

    @property
    def has_postal_code(self) -> bool:
        return self.field_is_set(self.postal_code)

    @property
    def missing_locality_or_administrative_area(self) -> bool:
        return self.field_is_missing(self.locality) or self.field_is_missing(self.administrative_area)

    @staticmethod
    def field_is_missing(field: Any) -> bool:
        return field is None or field == ''

    def field_is_set(self, field: Any) -> bool:
        return not self.field_is_missing(field)

    def ensure_enough_info(self) -> None:
        if self.field_is_missing(self.country):
            raise UnprocessableEntityError('Country field is required.')

        if self.field_is_missing(self.freeform) and self.field_is_missing(self.address1):
            raise UnprocessableEntityError('Either freeform or address1 is required.')

        if self.language is not None:
            LanguageMode.from_value(self.language)

    def add_custom_parameter(self, parameter: str, value: Any) -> None:
        self.custom_parameter_array[parameter] = value
