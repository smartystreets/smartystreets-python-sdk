class SmartyException(Exception):
    pass


class BadCredentialsError(SmartyException):
    pass


class PaymentRequiredError(SmartyException):
    pass


class RequestEntityTooLargeError(SmartyException):
    pass


class BadRequestError(SmartyException):
    pass


class TooManyRequestsError(SmartyException):
    pass


class InternalServerError(SmartyException):
    pass


class ServiceUnavailableError(SmartyException):
    pass
