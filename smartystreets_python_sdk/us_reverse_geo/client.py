from smartystreets_python_sdk import Request
from smartystreets_python_sdk.us_reverse_geo import Response


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_reverse_geo_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup, auth_id=None, auth_token=None):
        """
        Sends a Lookup object to the US Reverse Geo API and stores the result in the Lookup's result field.

        :param lookup: Lookup object with coordinates
        :param auth_id: Optional per-request auth_id for multi-tenant scenarios
        :param auth_token: Optional per-request auth_token for multi-tenant scenarios
        """
        request = self.build_request(lookup)

        if auth_id and auth_token:
            import base64
            credentials = "{}:{}".format(auth_id, auth_token)
            encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('ascii')
            request.headers['Authorization'] = 'Basic {}'.format(encoded_credentials)

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
        self.add_parameter(request, 'source', lookup.source)

        for parameter in lookup.custom_parameter_array:
            self.add_parameter(request, parameter, lookup.custom_parameter_array[parameter])

        return request

    @staticmethod
    def add_parameter(request, key, value):
        if value and value != 'none':
            request.parameters[key] = value
