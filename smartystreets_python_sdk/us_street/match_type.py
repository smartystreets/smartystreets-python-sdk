from enum import Enum


class MatchType(str, Enum):
    STRICT = "strict"
    RANGE = "range"  # Deprecated
    INVALID = "invalid"
    ENHANCED = "enhanced"
