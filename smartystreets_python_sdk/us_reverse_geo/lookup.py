from typing import Any, cast

from smartystreets_python_sdk.us_reverse_geo.result import Result
from smartystreets_python_sdk.us_reverse_geo.source import Source


class Lookup:
    def __init__(self, latitude: float | None = None, longitude: float | None = None,
                 source: Source | str | None = None) -> None:
        """
        In addition to holding the lat/lon data for this lookup, this class also will contain the
        result of the lookup after it comes back from the API.

        See https://smartystreets.com/docs/cloud/us-reverse-geo-api#http-input-fields
        """
        self.results: list[Result] = []
        self.custom_parameter_array: dict[str, Any] = {}
        self.latitude = round(cast(float, latitude), 8)
        self.longitude = round(cast(float, longitude), 8)
        self.source = source

    def add_custom_parameter(self, parameter: str, value: Any) -> None:
        self.custom_parameter_array[parameter] = value