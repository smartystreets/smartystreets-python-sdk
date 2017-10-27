from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.us_autocomplete import Suggestion, geolocation_type


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_autocomplete_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        """
        Sends a Lookup object to the US Autocomplete API and stores the result in the Lookup's result field.
        """
        if not lookup or not lookup.prefix:
            raise SmartyException('Send() must be passed a Lookup with the prefix field set.')

        request = self.build_request(lookup)

        response = self.sender.send(request)

        if response.error:
            raise response.error

        result = self.serializer.deserialize(response.payload)
        suggestions = self.convert_suggestions(result.get('suggestions', []))
        lookup.result = suggestions

        return suggestions

    def build_request(self, lookup):
        request = Request()

        self.add_parameter(request, 'prefix', lookup.prefix)
        self.add_parameter(request, 'suggestions', lookup.max_suggestions)
        self.add_parameter(request, 'city_filter', self.build_filter_string(lookup.city_filter))
        self.add_parameter(request, 'state_filter', self.build_filter_string(lookup.state_filter))
        self.add_parameter(request, 'prefer', self.build_filter_string(lookup.prefer))
        self.add_parameter(request, 'prefer_ratio', lookup.prefer_ratio)
        if lookup.geolocate_type is not geolocation_type.NONE:
            request.parameters['geolocate'] = 'true'
            request.parameters['geolocate_precision'] = lookup.geolocate_type
        else:
            request.parameters['geolocate'] = 'false'

        return request

    @staticmethod
    def build_filter_string(filter_list):
        return ','.join(filter_list or []) or None

    @staticmethod
    def convert_suggestions(suggestion_dictionaries):
        return [Suggestion(suggestion) for suggestion in suggestion_dictionaries]

    @staticmethod
    def add_parameter(request, key, value):
        if value and value is not 'none':
            request.parameters[key] = value
