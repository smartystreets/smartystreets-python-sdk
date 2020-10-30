from .result import Result


class Response:
    def __init__(self, obj):
        self.results = [Result(obj.get("results", {}))]
