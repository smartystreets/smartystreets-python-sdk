from .result import Result


class Response:
    def __init__(self, obj: dict) -> None:
        self.results: list[Result] = []
        for result in obj.get('results', []):
            self.results.append(Result(result))
