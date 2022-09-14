from smartystreets_python_sdk import Response


class FailingSender:
    def __init__(self, status_codes, error=None):
        self.status_codes = status_codes
        self.current_status_code_index = 0
        self.error_body = error

    def send(self, request):
        response = Response(None, self.status_codes[self.current_status_code_index], None, self.error_body)
        self.current_status_code_index += 1

        return response
