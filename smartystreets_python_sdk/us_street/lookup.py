from smartystreets_python_sdk.us_street.match_type import MatchType
from smartystreets_python_sdk.us_street.output_format import OutputFormat
from smartystreets_python_sdk.us_street.candidate import Candidate
from typing import Any
import json


class Lookup:
    def __init__(self, street: str | None = None, street2: str | None = None, secondary: str | None = None,
                 city: str | None = None, state: str | None = None, zipcode: str | None = None,
                 lastline: str | None = None, addressee: str | None = None, urbanization: str | None = None,
                 match: MatchType | str | None = None, candidates: int = 0, input_id: str | None = None,
                 outputformat: OutputFormat | str = OutputFormat.DEFAULT, county_source: str | None = None) -> None:
        """
        In addition to holding all input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/us-street-api#input-fields"
        """
        self.result: list[Candidate] = []
        self.custom_parameter_array: dict[str, Any] = {}
        self.input_id = input_id
        self.street = street
        self.street2 = street2
        self.secondary = secondary
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.lastline = lastline
        self.addressee = addressee
        self.urbanization = urbanization
        self.match = match
        self.candidates = candidates
        self.outputformat = outputformat
        self.county_source = county_source

    def add_custom_parameter(self, parameter: str, value: Any) -> None:
        self.custom_parameter_array[parameter] = value

    def to_dict(self) -> dict[str, Any]:
        result =  {
            "input_id": self.input_id,
            "street": self.street,
            "street2": self.street2,
            "secondary": self.secondary,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "lastline": self.lastline,
            "addressee": self.addressee,
            "urbanization": self.urbanization,
            "match": self.match,
            "candidates": self.candidates,
            "outputformat": self.outputformat,
            "county_source": self.county_source,
            "result": [candidate.to_dict() for candidate in self.result],
            "custom_parameter_array": self.custom_parameter_array
        }
        return {k: v for k, v in result.items() if v is not None}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())