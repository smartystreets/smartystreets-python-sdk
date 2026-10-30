import re

from smartystreets_python_sdk.exceptions import UnprocessableEntityError

_WHOLE_NUMBER = re.compile(r'\s*[+-]?\d+\s*')


def normalize_max_results(value):
    """
    Shared handling for the max_results input: accepts a whole number (or a string holding one),
    and returns it as an int only when it is above 0. Returns None when it shouldn't be sent
    (unset, blank, or 0 and below); anything that isn't a whole number raises.
    """
    if value is None or (isinstance(value, str) and not value.strip()):
        return None

    number = None
    if isinstance(value, bool):
        number = None
    elif isinstance(value, int):
        number = value
    elif isinstance(value, float) and value.is_integer():
        number = int(value)
    elif isinstance(value, str) and _WHOLE_NUMBER.fullmatch(value):
        number = int(value)

    if number is None:
        raise UnprocessableEntityError("invalid max_results value; must be a whole number")

    return number if number > 0 else None
