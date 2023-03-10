from enum import StrEnum


class MatchType(StrEnum):
    STRICT = "strict"
    RANGE = "range"  # Deprecated
    INVALID = "invalid"
    ENHANCED = "enhanced"
