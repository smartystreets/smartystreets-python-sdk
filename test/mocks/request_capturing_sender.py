from smartystreets_python_sdk import Response


class RequestCapturingSender:
    def __init__(self):
        self.request = None

    def send(self, request):
        self.request = request

        return Response("[]", 200)
