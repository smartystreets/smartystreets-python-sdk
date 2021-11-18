from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.us_autocomplete_pro import Suggestion, geolocation_type


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_autocomplete_pro_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        """
        Sends a Lookup object to the US Autocomplete Pro API and stores the result in the Lookup's result field.
        """
        if not lookup or not lookup.search:
            raise SmartyException('Send() must be passed a Lookup with the search field set.')

        request = self.build_request(lookup)

        response = self.sender.send(request)

        if response.error:
            raise response.error

        result = self.serializer.deserialize(response.payload)
        suggestions = self.convert_suggestions(result.get('suggestions') or [])
        lookup.result = suggestions

        return suggestions

    def build_request(self, lookup):
        request = Request()

        self.add_parameter(request, 'search', lookup.search)
        self.add_parameter(request, 'max_results', lookup.max_results)
        self.add_parameter(request, 'include_only_cities', self.build_filter_string(lookup.city_filter))
        self.add_parameter(request, 'include_only_states', self.build_filter_string(lookup.state_filter))
        self.add_parameter(request, 'include_only_zip_codes', self.build_filter_string(lookup.zip_filter))
        self.add_parameter(request, 'exclude_states', self.build_filter_string(lookup.exclude))
        self.add_parameter(request, 'prefer_cities', self.build_filter_string(lookup.prefer_cities))
        self.add_parameter(request, 'prefer_states', self.build_filter_string(lookup.prefer_states))
        self.add_parameter(request, 'prefer_zip_codes', self.build_filter_string(lookup.prefer_zips))
        self.add_parameter(request, 'prefer_ratio', lookup.prefer_ratio)
        self.add_parameter(request, 'prefer_geolocation', lookup.prefer_geo)
        self.add_parameter(request, 'selected', lookup.selected)
        self.add_parameter(request, 'source', lookup.source)

        return request

    @staticmethod
    def build_filter_string(filter_list):
        return ';'.join(filter_list or []) or None

    @staticmethod
    def convert_suggestions(suggestion_dictionaries):
        return [Suggestion(suggestion) for suggestion in suggestion_dictionaries]

    @staticmethod
    def add_parameter(request, key, value):
        if value and value != 'none':
            request.parameters[key] = value
