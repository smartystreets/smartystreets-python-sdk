from .result import Result


class Response:
    def __init__(self, obj):
        self.results = []
        for result in obj.get('results', []):
            self.results.append(Result(result))
