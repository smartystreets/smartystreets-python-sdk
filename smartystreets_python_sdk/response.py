class Response:
    def __init__(self, payload, status_code, error=None):
        self.payload = payload
        self.status_code = status_code
        self.error = error
