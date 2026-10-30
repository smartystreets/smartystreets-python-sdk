from enum import Enum

from smartystreets_python_sdk.exceptions import UnprocessableEntityError


class LanguageMode(Enum):
    """
    A closed set of valid Language values, the closest Python equivalent to an enum-constrained field.
    """
    NATIVE = 'native'
    LATIN = 'latin'

    @staticmethod
    def from_value(value):
        """
        Resolves a LanguageMode instance or a raw value (eg. from user input or config) into a LanguageMode,
        matching 'native'/'latin' regardless of case.
        """
        if isinstance(value, LanguageMode):
            return value

        for mode in LanguageMode:
            if str(value).lower() == mode.value:
                return mode

        raise UnprocessableEntityError(
            "invalid Language value; must be unset, 'native', or 'latin' (case-insensitive)")
