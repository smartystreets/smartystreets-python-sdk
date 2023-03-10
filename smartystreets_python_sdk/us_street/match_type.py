from enum import StrEnum


class MatchType(StrEnum):
    strict = "strict"
    range = "range"  # Deprecated
    invalid = "invalid"
    enhanced = "enhanced"
