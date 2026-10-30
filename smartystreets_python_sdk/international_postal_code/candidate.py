class Candidate:
    def __init__(self, obj: dict | None = None) -> None:
        obj = obj or {}
        self.input_id: str | None = obj.get('input_id', None)
        self.administrative_area: str | None = obj.get('administrative_area', None)
        self.sub_administrative_area: str | None = obj.get('sub_administrative_area', None)
        self.super_administrative_area: str | None = obj.get('super_administrative_area', None)
        self.country_iso_3: str | None = obj.get('country_iso_3', None)
        self.locality: str | None = obj.get('locality', None)
        self.dependent_locality: str | None = obj.get('dependent_locality', None)
        self.dependent_locality_name: str | None = obj.get('dependent_locality_name', None)
        self.double_dependent_locality: str | None = obj.get('double_dependent_locality', None)
        self.postal_code: str | None = obj.get('postal_code', None)
        self.postal_code_extra: str | None = obj.get('postal_code_extra', None)
        self.thoroughfare: str | None = obj.get('thoroughfare', None)
