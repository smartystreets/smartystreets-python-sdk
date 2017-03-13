from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import UnprocessableEntityError
from smartystreets_python_sdk.international_street import Candidate


class Client:
    def __init__(self, sender, serializer):
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup):
        self.ensure_enough_info(lookup)
        request = self.build_request(lookup)

        response = self.sender.send(request)

        candidates = self.convert_candidates(self.serializer.deserialize(response.payload))
        lookup.result = candidates
        return candidates

    def build_request(self, lookup):
        request = Request()

        request.parameters['country'] = lookup.country
        request.parameters['geocode'] = str(lookup.geocode).lower()
        request.parameters['language'] = lookup.language
        request.parameters['freeform'] = lookup.freeform
        request.parameters['address1'] = lookup.address1
        request.parameters['address2'] = lookup.address2
        request.parameters['address3'] = lookup.address3
        request.parameters['address4'] = lookup.address4
        request.parameters['organization'] = lookup.organization
        request.parameters['locality'] = lookup.locality
        request.parameters['administrative_area'] = lookup.administrative_area
        request.parameters['postal_code'] = lookup.postal_code

        return request

    def ensure_enough_info(self, lookup):
        if lookup.missing_country():
            raise UnprocessableEntityError('Country field is required.')

        if lookup.has_freeform():
            return True

        if lookup.missing_address1():
            raise UnprocessableEntityError('Either freeform or address1 is required.')

        if lookup.has_postal_code():
            return True

        if lookup.missing_locality_or_administrative_area():
            raise UnprocessableEntityError('Insufficient information: One or more required fields were not set on the lookup.')

    def convert_candidates(self, raw_candidates):
        converted_candidates = []

        for candidate in raw_candidates:
            converted_candidates.append(Candidate(candidate))

        return converted_candidates
