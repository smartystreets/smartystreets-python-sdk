from smartystreets_python_sdk import Request
from smartystreets_python_sdk.international_street import Candidate


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_international_street_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        """
        Sends a Lookup object to the International Street API and stores the result in the Lookup's result field.
        """
        lookup.ensure_enough_info()
        request = self.build_request(lookup)

        response = self.sender.send(request)

        candidates = self.convert_candidates(self.serializer.deserialize(response.payload))
        lookup.result = candidates
        return candidates

    def build_request(self, lookup):
        request = Request()

        self.add_parameter(request, 'country', lookup.country)
        self.add_parameter(request, 'geocode', str(lookup.geocode).lower())
        self.add_parameter(request, 'language', lookup.language)
        self.add_parameter(request, 'freeform', lookup.freeform)
        self.add_parameter(request, 'address1', lookup.address1)
        self.add_parameter(request, 'address2', lookup.address2)
        self.add_parameter(request, 'address3', lookup.address3)
        self.add_parameter(request, 'address4', lookup.address4)
        self.add_parameter(request, 'organization', lookup.organization)
        self.add_parameter(request, 'locality', lookup.locality)
        self.add_parameter(request, 'administrative_area', lookup.administrative_area)
        self.add_parameter(request, 'postal_code', lookup.postal_code)

        return request

    @staticmethod
    def convert_candidates(raw_candidates):
        return [Candidate(candidate) for candidate in raw_candidates]

    @staticmethod
    def add_parameter(request, key, value):
        if value and value is not 'none':
            request.parameters[key] = value
