import json

from typing import Any

from smartystreets_python_sdk import errors, exceptions
from .protocols import Sender
from .request import Request
from .response import Response


class StatusCodeSender:
    def __init__(self, inner: Sender) -> None:
        self.inner = inner

    def parse_rate_limit_response(self, response: Response) -> exceptions.SmartyException:
        return messageFrom(response, exceptions.TooManyRequestsError(errors.TOO_MANY_REQUESTS))

    def send(self, request: Request) -> Response:
        response = self.inner.send(request)

        if not response.error:
            if response.status_code == 429:
                response.error = self.parse_rate_limit_response(response)
            elif response.status_code not in (200, 304):
                response.error = messageFrom(response, fallback_error(response.status_code))

        return response

def fallback_error(status_code: int) -> exceptions.SmartyException:
    error = statuses.get(status_code)
    if error is None:
        error = exceptions.SmartyException(
            'The server returned an unexpected HTTP status code: {}'.format(status_code))
    return error


def messageFrom(response: Response, fallback: exceptions.SmartyException) -> exceptions.SmartyException:
    message = extract_message(response)
    if message:
        return type(fallback)(message)
    return type(fallback)('{} Body: {}'.format(fallback, unused_body(response)).rstrip())


def unused_body(response: Response) -> str:
    payload = response.payload
    if payload is None:
        return ''
    if isinstance(payload, bytes):
        payload = payload.decode('utf-8', 'replace')
    return str(payload).strip()


def extract_message(response: Response) -> str:
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


def bad_credentials() -> exceptions.SmartyException:
    return exceptions.BadCredentialsError(errors.BAD_CREDENTIALS)


def payment_required() -> exceptions.SmartyException:
    return exceptions.PaymentRequiredError(errors.PAYMENT_REQUIRED)


def forbidden() -> exceptions.SmartyException:
    return exceptions.ForbiddenError(errors.FORBIDDEN)


def request_timeout() -> exceptions.SmartyException:
    return exceptions.RequestTimeoutError(errors.REQUEST_TIMEOUT)


def request_entity_too_large() -> exceptions.SmartyException:
    return exceptions.RequestEntityTooLargeError(errors.REQUEST_ENTITY_TOO_LARGE)


def bad_request() -> exceptions.SmartyException:
    return exceptions.BadRequestError(errors.BAD_REQUEST)


def unprocessable_entity() -> exceptions.SmartyException:
    return exceptions.UnprocessableEntityError(errors.UNPROCESSABLE_ENTITY)


def internal_server_error() -> exceptions.SmartyException:
    return exceptions.InternalServerError(errors.INTERNAL_SERVER_ERROR)


def bad_gateway() -> exceptions.SmartyException:
    return exceptions.BadGatewayError(errors.BAD_GATEWAY)


def service_unavailable() -> exceptions.SmartyException:
    return exceptions.ServiceUnavailableError(errors.SERVICE_UNAVAILABLE)


def gateway_timeout() -> exceptions.SmartyException:
    return exceptions.GatewayTimeoutError(errors.GATEWAY_TIMEOUT)


statuses: dict[int, exceptions.SmartyException] = {401: bad_credentials(),
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
