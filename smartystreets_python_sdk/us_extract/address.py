from smartystreets_python_sdk.us_street.candidate import Candidate


class Address:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-extract-api#http-response-status"
        """
        self.text = obj.get('text', None)
        self.verified = obj.get('verified', None)
        self.line = obj.get('line', None)
        self.start = obj.get('start', None)
        self.end = obj.get('end', None)
        candidates = obj.get('api_output', [])
        self.candidates = []

        for candidate in candidates:
            self.candidates.append(Candidate(candidate))
