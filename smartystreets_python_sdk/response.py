class Response:
    def __init__(self, payload, status_code, headers=None, error=None):
        self.payload = payload
        self.status_code = status_code
        self.headers = headers
        self.error = error

    def getHeader(self, header):
        if self.headers is None:
            return None
        else:
            return self.headers[header]
