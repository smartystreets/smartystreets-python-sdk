import json

from smartystreets_python_sdk import errors, exceptions


class StatusCodeSender:
    def __init__(self, inner):
        self.inner = inner

    def parse_rate_limit_response(self, response):
        return messageFrom(response, exceptions.TooManyRequestsError(errors.TOO_MANY_REQUESTS))

    def send(self, request):
        response = self.inner.send(request)

        if not response.error:
            if response.status_code == 429:
                response.error = self.parse_rate_limit_response(response)
            elif response.status_code not in (200, 304):
                response.error = messageFrom(response, fallback_error(response.status_code))

        return response

def fallback_error(status_code):
    error = statuses.get(status_code)
    if error is None:
        error = exceptions.SmartyException(
            'The server returned an unexpected HTTP status code: {}'.format(status_code))
    return error


def messageFrom(response, fallback):
    message = extract_message(response)
    if message:
        return type(fallback)(message)
    return type(fallback)('{} Body: {}'.format(fallback, unused_body(response)).rstrip())


def unused_body(response):
    payload = response.payload
    if payload is None:
        return ''
    if isinstance(payload, bytes):
        payload = payload.decode('utf-8', 'replace')
    return str(payload).strip()


def extract_message(response):
    try:
        response_json = json.loads(response.payload)
    except (ValueError, TypeError):
        return ''
    if response_json is None:
        return ''
    errors_json = response_json.get('errors')
    if errors_json is None:
        return ''
    message = ''
    for current_error in errors_json:
        current_message = current_error.get('message')
        if current_message is not None:
            message = message + current_message + ' '
    return message.rstrip()


def bad_credentials():
    return exceptions.BadCredentialsError(errors.BAD_CREDENTIALS)


def payment_required():
    return exceptions.PaymentRequiredError(errors.PAYMENT_REQUIRED)


def forbidden():
    return exceptions.ForbiddenError(errors.FORBIDDEN)


def request_timeout():
    return exceptions.RequestTimeoutError(errors.REQUEST_TIMEOUT)


def request_entity_too_large():
    return exceptions.RequestEntityTooLargeError(errors.REQUEST_ENTITY_TOO_LARGE)


def bad_request():
    return exceptions.BadRequestError(errors.BAD_REQUEST)


def unprocessable_entity():
    return exceptions.UnprocessableEntityError(errors.UNPROCESSABLE_ENTITY)


def internal_server_error():
    return exceptions.InternalServerError(errors.INTERNAL_SERVER_ERROR)


def bad_gateway():
    return exceptions.BadGatewayError(errors.BAD_GATEWAY)


def service_unavailable():
    return exceptions.ServiceUnavailableError(errors.SERVICE_UNAVAILABLE)


def gateway_timeout():
    return exceptions.GatewayTimeoutError(errors.GATEWAY_TIMEOUT)


statuses = {401: bad_credentials(),
            402: payment_required(),
            403: forbidden(),
            408: request_timeout(),
            413: request_entity_too_large(),
            400: bad_request(),
            422: unprocessable_entity(),
            500: internal_server_error(),
            502: bad_gateway(),
            503: service_unavailable(),
            504: gateway_timeout()
            }
