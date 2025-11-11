class Candidate:
    def __init__(self, obj=None):
        obj = obj or {}
        self.input_id = obj.get('input_id', None)
        self.administrative_area = obj.get('administrative_area', None)
        self.sub_administrative_area = obj.get('sub_administrative_area', None)
        self.super_administrative_area = obj.get('super_administrative_area', None)
        self.country_iso_3 = obj.get('country_iso_3', None)
        self.locality = obj.get('locality', None)
        self.dependent_locality = obj.get('dependent_locality', None)
        self.dependent_locality_name = obj.get('dependent_locality_name', None)
        self.double_dependent_locality = obj.get('double_dependent_locality', None)
        self.postal_code = obj.get('postal_code', None)
        self.postal_code_extra = obj.get('postal_code_extra', None)
