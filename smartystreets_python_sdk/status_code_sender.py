import errors


class StatusCodeSender:
    def __init__(self, inner):
        self.inner = inner

    def send(self, request):
        response = self.inner.send(request)

        response.status = statuses[response.status_code]

        return response

statuses = {200: "OK",
            401: errors.BAD_CREDENTIALS,
            402: errors.PAYMENT_REQUIRED,
            413: errors.REQUEST_ENTITY_TOO_LARGE,
            400: errors.BAD_REQUEST,
            429: errors.TOO_MANY_REQUESTS,
            500: errors.INTERNAL_SERVER_ERROR,
            503: errors.SERVICE_UNAVAILABLE
            }
