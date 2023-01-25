from enum import Enum, auto


class InternationalGeolocateType(Enum):
    admin_area = "admin_area"
    locality = "locality"
    postal_code = "postal_code"
    geocodes = "geocodes"
    none = ""
