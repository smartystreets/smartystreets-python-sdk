from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.international_autocomplete import Suggestion


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_autocomplete_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        """
        Sends a Lookup object to the International Autocomplete API and stores the result in the Lookup's result field.
        """
        if not lookup or not lookup.search:
            raise SmartyException('Send() must be passed a Lookup with the search field set.')

        request = self.build_request(lookup)

        response = self.sender.send(request)

        if response.error:
            raise response.error

        result = self.serializer.deserialize(response.payload)
        suggestions = self.convert_suggestions(result or [])
        lookup.result = suggestions

        return suggestions

    def build_request(self, lookup):
        request = Request()

        self.add_parameter(request, 'country', lookup.country)
        self.add_parameter(request, 'search', lookup.search)
        self.add_parameter(request, 'include_only_administrative_area', lookup.administrative_area)
        self.add_parameter(request, 'include_only_locality', lookup.locality)
        self.add_parameter(request, 'include_only_postal_code', lookup.postal_code)

        return request

    @staticmethod
    def convert_suggestions(suggestion_dictionaries):
        return [Suggestion(suggestion) for suggestion in suggestion_dictionaries]

    @staticmethod
    def add_parameter(request, key, value):
        if value and value != 'none':
            request.parameters[key] = value
