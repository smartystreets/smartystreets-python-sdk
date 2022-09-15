import json

from smartystreets_python_sdk import errors, exceptions


class StatusCodeSender:
    def __init__(self, inner):
        self.inner = inner

    def parse_rate_limit_response(self, response):
        error_message = exceptions.TooManyRequestsError(errors.TOO_MANY_REQUESTS)
        response_json = json.loads(response.payload)
        if response_json is not None:
            errors_json = response_json.get('errors')
            if errors_json is not None:
                message = ''
                for current_error in errors_json:
                    current_message = current_error.get('message')
                    if current_message is not None:
                        message = message + current_message + ' '
                error_message = exceptions.TooManyRequestsError(message.rstrip())
        return error_message

    def send(self, request):
        response = self.inner.send(request)

        if not response.error:
            if response.status_code != 429:
                response.error = statuses.get(response.status_code)
            else:
                response.error = self.parse_rate_limit_response(response)

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
            500: internal_server_error(),
            503: service_unavailable(),
            504: gateway_timeout()
            }
