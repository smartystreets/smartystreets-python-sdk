from smartystreets_python_sdk import Request
from smartystreets_python_sdk.international_postal_code import Candidate
from smartystreets_python_sdk.international_postal_code.lookup import Lookup
from smartystreets_python_sdk.international_postal_code.language_mode import LanguageMode
from smartystreets_python_sdk.max_results import normalize_max_results
from smartystreets_python_sdk.protocols import Sender, Serializer
from typing import Any, cast

class Client:
    def __init__(self, sender: Sender, serializer: Serializer) -> None:
        """
        It is recommended to instantiate this class using ClientBuilder.build_international_postal_code_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send(self, lookup: Lookup) -> list[Candidate]:
        if not lookup:
            raise ValueError("Send() must be passed a Lookup object with required fields set.")
        request = self.build_request(lookup)
        response = self.sender.send(request)
        if getattr(response, 'error', None):
            raise cast(Exception, response.error)
        candidates = self.convert_candidates(self.serializer.deserialize(response.payload))
        lookup.results = candidates
        return candidates

    def build_request(self, lookup: Lookup) -> Request:
        request = Request()
        self.add_parameter(request, 'input_id', lookup.input_id)
        self.add_parameter(request, 'country', lookup.country)
        self.add_parameter(request, 'language', self.normalized_language(lookup.language))
        self.add_parameter(request, 'locality', lookup.locality)
        self.add_parameter(request, 'administrative_area', lookup.administrative_area)
        self.add_parameter(request, 'postal_code', lookup.postal_code)
        self.add_parameter(request, 'max_results', normalize_max_results(lookup.max_results))
        return request

    @staticmethod
    def convert_candidates(candidate_dicts: list[dict[str, Any]] | None) -> list[Candidate]:
        return [Candidate(obj) for obj in (candidate_dicts or [])]

    @staticmethod
    def add_parameter(request: Request, key: str, value: Any) -> None:
        if value and value != 'none':
            request.parameters[key] = value

    @staticmethod
    def normalized_language(language):
        if language is None:
            return None
        return LanguageMode.from_value(language).value
