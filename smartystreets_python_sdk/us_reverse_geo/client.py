from smartystreets_python_sdk import Request
from smartystreets_python_sdk.us_reverse_geo import Response


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_reverse_geo_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        """
        Sends a Lookup object to the US Reverse Geo API and stores the result in the Lookup's result field.
        """
        request = self.build_request(lookup)

        response = self.sender.send(request)

        if response.error is not None:
            raise response.error

        results = Response(self.serializer.deserialize(response.payload)).results
        lookup.results = results

        return results

    def build_request(self, lookup):
        request = Request()

        self.add_parameter(request, 'latitude', lookup.latitude)
        self.add_parameter(request, 'longitude', lookup.longitude)

        return request

    @staticmethod
    def add_parameter(request, key, value):
        if value and value != 'none':
            request.parameters[key] = value
