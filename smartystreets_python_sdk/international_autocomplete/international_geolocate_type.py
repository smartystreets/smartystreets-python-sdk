from enum import StrEnum


class InternationalGeolocateType(StrEnum):
    admin_area = "admin_area"
    locality = "locality"
    postal_code = "postal_code"
    geocodes = "geocodes"
    none = ""
