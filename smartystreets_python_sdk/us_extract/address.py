from smartystreets_python_sdk.us_street.candidate import Candidate


class Address:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-extract-api#http-response-status"
        """
        self.text: str | None = obj.get('text', None)
        self.verified: bool | None = obj.get('verified', None)
        self.line: int | None = obj.get('line', None)
        self.start: int | None = obj.get('start', None)
        self.end: int | None = obj.get('end', None)
        candidates = obj.get('api_output', [])
        self.candidates: list[Candidate] = []

        for candidate in candidates:
            self.candidates.append(Candidate(candidate))
