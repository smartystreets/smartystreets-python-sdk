from enum import Enum


class MatchType(str, Enum):
    STRICT = "strict"
    INVALID = "invalid"
    ENHANCED = "enhanced"
