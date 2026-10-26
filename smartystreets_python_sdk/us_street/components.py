class Components:
    def __init__(self, obj: dict) -> None:
        """
        This class contains the matched address broken down into its fundamental pieces.

        See "https://smartystreets.com/docs/cloud/us-street-api#components"
        """
        self.urbanization: str | None = obj.get('urbanization', None)
        self.primary_number: str | None = obj.get('primary_number', None)
        self.street_name: str | None = obj.get('street_name', None)
        self.street_predirection: str | None = obj.get('street_predirection', None)
        self.street_postdirection: str | None = obj.get('street_postdirection', None)
        self.street_suffix: str | None = obj.get('street_suffix', None)
        self.secondary_number: str | None = obj.get('secondary_number', None)
        self.secondary_designator: str | None = obj.get('secondary_designator', None)
        self.extra_secondary_number: str | None = obj.get('extra_secondary_number', None)
        self.extra_secondary_designator: str | None = obj.get('extra_secondary_designator', None)
        self.pmb_designator: str | None = obj.get('pmb_designator', None)
        self.pmb_number: str | None = obj.get('pmb_number', None)
        self.city_name: str | None = obj.get('city_name', None)
        self.default_city_name: str | None = obj.get('default_city_name', None)
        self.state_abbreviation: str | None = obj.get('state_abbreviation', None)
        self.zipcode: str | None = obj.get('zipcode', None)
        self.plus4_code: str | None = obj.get('plus4_code', None)
        self.delivery_point: str | None = obj.get('delivery_point', None)
        self.delivery_point_check_digit: str | None = obj.get('delivery_point_check_digit', None)

    def to_dict(self) -> dict:
        result = {
            "urbanization": self.urbanization,
            "primary_number": self.primary_number,
            "street_name": self.street_name,
            "street_predirection": self.street_predirection,
            "street_postdirection": self.street_postdirection,
            "street_suffix": self.street_suffix,
            "secondary_number": self.secondary_number,
            "secondary_designator": self.secondary_designator,
            "extra_secondary_number": self.extra_secondary_number,
            "extra_secondary_designator": self.extra_secondary_designator,
            "pmb_designator": self.pmb_designator,
            "pmb_number": self.pmb_number,
            "city_name": self.city_name,
            "default_city_name": self.default_city_name,
            "state_abbreviation": self.state_abbreviation,
            "zipcode": self.zipcode,
            "plus4_code": self.plus4_code,
            "delivery_point": self.delivery_point,
            "delivery_point_check_digit": self.delivery_point_check_digit
        }
        return {k: v for k, v in result.items() if v is not None}
