from typing import cast


class Candidate:
    def __init__(self, obj: dict | None = None) -> None:
        obj = cast(dict, obj)
        self.street: str | None = obj.get('street', None)
        self.locality: str | None = obj.get('locality', None)
        self.administrative_area: str | None = obj.get('administrative_area', None)
        self.administrative_area_short: str | None = obj.get('administrative_area_short', None)
        self.administrative_area_long: str | None = obj.get('administrative_area_long', None)
        self.postal_code: str | None = obj.get('postal_code', None)
        self.country_iso3: str | None = obj.get('country_iso3', None)
        # v2 fields
        self.entries: int | None = obj.get('entries', None)
        self.address_text: str | None = obj.get('address_text', None)
        self.address_id: str | None = obj.get('address_id', None)
