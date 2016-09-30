from smartystreets_python_sdk import Response


class MockExceptionSender:
    def __init__(self, exception):
        self.exception = exception

    def send(self, request):
        if not self.exception:
            return None
        else:
            return Response(None, None, self.exception)
