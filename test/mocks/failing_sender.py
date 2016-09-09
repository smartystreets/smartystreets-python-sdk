from smartystreets_python_sdk import Response


class FailingSender:
    def __init__(self, status_codes):
        self.status_codes = status_codes
        self.current_status_code_index = 0

    def send(self, request):
        response = Response(None, self.status_codes[self.current_status_code_index])
        self.current_status_code_index += 1

        return response
