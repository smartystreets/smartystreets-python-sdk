from smartystreets_python_sdk import errors, exceptions


class StatusCodeSender:
    def __init__(self, inner):
        self.inner = inner

    def send(self, request):
        response = self.inner.send(request)

        if not response.error:
            response.error = statuses.get(response.status_code)

        return response


def ok():
    return None


def bad_credentials():
    return exceptions.BadCredentialsError(errors.BAD_CREDENTIALS)


def payment_required():
    return exceptions.PaymentRequiredError(errors.PAYMENT_REQUIRED)


def forbidden():
    return exceptions.ForbiddenError(errors.FORBIDDEN)


def request_entity_too_large():
    return exceptions.RequestEntityTooLargeError(errors.REQUEST_ENTITY_TOO_LARGE)


def bad_request():
    return exceptions.BadRequestError(errors.BAD_REQUEST)


def unprocessable_entity():
    return exceptions.UnprocessableEntityError(errors.UNPROCESSABLE_ENTITY)


def too_many_requests():
    return exceptions.TooManyRequestsError(errors.TOO_MANY_REQUESTS)


def internal_server_error():
    return exceptions.InternalServerError(errors.INTERNAL_SERVER_ERROR)


def service_unavailable():
    return exceptions.ServiceUnavailableError(errors.SERVICE_UNAVAILABLE)


def gateway_timeout():
    return exceptions.GatewayTimeoutError(errors.GATEWAY_TIMEOUT)


statuses = {200: ok(),
            401: bad_credentials(),
            402: payment_required(),
            403: forbidden(),
            413: request_entity_too_large(),
            400: bad_request(),
            422: unprocessable_entity(),
            429: too_many_requests(),
            500: internal_server_error(),
            503: service_unavailable(),
            504: gateway_timeout()
            }
