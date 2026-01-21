from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from smartystreets_python_sdk.international_autocomplete import Candidate


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_international_autocomplete_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup, auth_id=None, auth_token=None):
        """
        Sends a Lookup object to the International Autocomplete API and stores the result in the Lookup's result field.

        :param lookup: Lookup object with search parameters
        :param auth_id: Optional per-request auth_id for multi-tenant scenarios
        :param auth_token: Optional per-request auth_token for multi-tenant scenarios
        """
        if not lookup or (not lookup.search and not lookup.address_id):
            raise SmartyException('Send() must be passed a Lookup with country set, and search or address_id set.')

        request = self.build_request(lookup)

        if auth_id and auth_token:
            import base64
            credentials = "{}:{}".format(auth_id, auth_token)
            encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('ascii')
            request.headers['Authorization'] = 'Basic {}'.format(encoded_credentials)

        response = self.sender.send(request)

        if response.error:
            raise response.error

        result = self.serializer.deserialize(response.payload)
        candidates = self.convert_candidates(result.get('candidates') or [])
        lookup.result = candidates

        return candidates

    def build_request(self, lookup):
        request = Request()

        if lookup.address_id is not None:
            request.url_components = "/" + lookup.address_id

        self.add_parameter(request, 'country', lookup.country)
        self.add_parameter(request, 'search', lookup.search)
        self.add_parameter(request, 'max_results', lookup.max_results)
        self.add_parameter(request, 'include_only_locality', lookup.locality)
        self.add_parameter(request, 'include_only_postal_code', lookup.postal_code)

        for parameter in lookup.custom_parameter_array:
            self.add_parameter(request, parameter, lookup.custom_parameter_array[parameter])

        return request

    @staticmethod
    def convert_candidates(candidate_dictionaries):
        return [Candidate(candidate) for candidate in candidate_dictionaries]

    @staticmethod
    def add_parameter(request, key, value):
        if value and value != 'none':
            request.parameters[key] = value
