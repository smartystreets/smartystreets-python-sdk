from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.us_extract import Result


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_extract_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        """
        Sends a Lookup object to the US Extract Code API and stores the result in the Lookup's result field.
        It also returns the result directly.
        """
        if lookup is None or lookup.text is None or not isinstance(lookup.text, str) or len(lookup.text.strip()) == 0:
            raise SmartyException('Client.send() requires a Lookup with the "text" field set')

        request = self.build_request(lookup)

        response = self.sender.send(request)
        if response.error:
            raise response.error

        result = Result(self.serializer.deserialize(response.payload))

        lookup.result = result
        return result

    @staticmethod
    def build_request(lookup):
        request = Request()
        request.content_type = 'text/plain'
        request.payload = lookup.text

        Client.add_parameter(request, 'html', str(lookup.html).lower())
        Client.add_parameter(request, 'aggressive', str(lookup.aggressive).lower())
        Client.add_parameter(request, 'addr_line_breaks', str(lookup.addresses_have_line_breaks).lower())
        Client.add_parameter(request, 'addr_per_line', lookup.addresses_per_line)

        return request

    @staticmethod
    def add_parameter(request, key, value):
        if value and value is not 'none':
            request.parameters[key] = value
