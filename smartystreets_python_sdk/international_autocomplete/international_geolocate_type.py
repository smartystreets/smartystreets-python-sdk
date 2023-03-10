from enum import StrEnum


class InternationalGeolocateType(StrEnum):
    ADMIN_AREA = "admin_area"
    LOCALITY = "locality"
    POSTAL_CODE = "postal_code"
    GEOCODES = "geocodes"
    NONE = ""
