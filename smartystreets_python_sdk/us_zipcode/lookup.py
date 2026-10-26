from typing import Any

from smartystreets_python_sdk.us_zipcode.result import Result


class Lookup:
    def __init__(self, city: str | None = None, state: str | None = None, zipcode: str | None = None,
                 input_id: str | None = None) -> None:
        """
        In addition to holding all of the input data for this lookup, this class also
            will contain the result of the lookup after it comes back from the API.
            
            See "https://smartystreets.com/docs/cloud/us-zipcode-api#http-request-input-fields"
        """
        self.result: Result | None = None
        self.custom_parameter_array: dict[str, Any] = {}
        self.input_id = input_id
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def add_custom_parameter(self, parameter: str, value: Any) -> None:
        self.custom_parameter_array[parameter] = value
