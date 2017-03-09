from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.us_autocomplete import Suggestion, geolocation_type


class Client:
    def __init__(self, sender, serializer):
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        if not lookup or not lookup.prefix:
            raise SmartyException('Send() must be passed a Lookup with the prefix field set.')

        request = self.build_request(lookup)

        response = self.sender.send(request)

        result = self.serializer.deserialize(response.payload)
        suggestions = self.convert_suggestions(result.get('suggestions', []))
        lookup.result = suggestions

        return suggestions

    def build_request(self, lookup):
        request = Request()

        request.parameters['prefix'] = lookup.prefix
        request.parameters['suggestions'] = lookup.max_suggestions
        request.parameters['city_filter'] = self.build_filter_string(lookup.city_filter)
        request.parameters['state_filter'] = self.build_filter_string(lookup.state_filter)
        request.parameters['prefer'] = self.build_filter_string(lookup.prefer)
        if lookup.geolocate_type is not geolocation_type.NONE:
            request.parameters['geolocate'] = 'true'
            request.parameters['geolocate_precision'] = lookup.geolocate_type
        else:
            request.parameters['geolocate'] = 'false'

        return request

    def build_filter_string(self, filter_list):
        if not filter_list:
            return None

        filter_string = ''

        for item in filter_list:
            filter_string += ("{},".format(item))

        if filter_string.endswith(','):
            filter_string = filter_string[:-1]

        return filter_string

    def convert_suggestions(self, suggestion_dictionaries):
        suggestion_objects = []

        for suggestion in suggestion_dictionaries:
            suggestion_objects.append(Suggestion(suggestion))

        return suggestion_objects
