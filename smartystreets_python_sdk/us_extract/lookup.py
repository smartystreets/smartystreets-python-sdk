from typing import Any

from smartystreets_python_sdk.us_street.match_type import MatchType
from smartystreets_python_sdk.us_extract.result import Result


class Lookup:
    def __init__(self, text: str | None = None, html: bool | str | None = None, aggressive: bool | str | None = None,
                 addresses_have_line_breaks: bool | str | None = None, addresses_per_line: int | None = None,
                 match: MatchType | str | None = MatchType.STRICT) -> None:
        """
        In addition to holding all input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/us-extract-api#http-request-input-fields"
        """
        self.result: Result | None = None
        self.custom_parameter_array: dict[str, Any] = {}
        self.text = text
        self.html = html
        self.aggressive = aggressive
        self.addresses_have_line_breaks = addresses_have_line_breaks
        self.addresses_per_line = addresses_per_line
        self.match = match

    def add_custom_parameter(self, parameter: str, value: Any) -> None:
        self.custom_parameter_array[parameter] = value

