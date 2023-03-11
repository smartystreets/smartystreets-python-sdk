from enum import Enum


class InternationalGeolocateType(str, Enum):
    ADMIN_AREA = "admin_area"
    LOCALITY = "locality"
    POSTAL_CODE = "postal_code"
    GEOCODES = "geocodes"
    NONE = ""
