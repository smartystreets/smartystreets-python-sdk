from smartystreets_python_sdk import Request
from smartystreets_python_sdk.international_postal_code import Candidate

class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_international_postal_code_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        if not lookup:
            raise ValueError("Send() must be passed a Lookup object with required fields set.")
        request = self.build_request(lookup)
        response = self.sender.send(request)
        if getattr(response, 'error', None):
            raise response.error
        candidates = self.convert_candidates(self.serializer.deserialize(response.payload))
        lookup.results = candidates
        return candidates

    def build_request(self, lookup):
        request = Request()
        self.add_parameter(request, 'input_id', lookup.input_id)
        self.add_parameter(request, 'country', lookup.country)
        self.add_parameter(request, 'locality', lookup.locality)
        self.add_parameter(request, 'administrative_area', lookup.administrative_area)
        self.add_parameter(request, 'postal_code', lookup.postal_code)
        return request

    @staticmethod
    def convert_candidates(candidate_dicts):
        return [Candidate(obj) for obj in (candidate_dicts or [])]

    @staticmethod
    def add_parameter(request, key, value):
        if value and value != 'none':
            request.parameters[key] = value
