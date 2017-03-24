class Components:
    def __init__(self, obj):
        """
        This class contains the matched address broken down into its fundamental pieces.

        See "https://smartystreets.com/docs/cloud/us-street-api#components"
        """
        self.urbanization = obj.get('urbanization', None)
        self.primary_number = obj.get('primary_number', None)
        self.street_name = obj.get('street_name', None)
        self.street_predirection = obj.get('street_predirection', None)
        self.street_postdirection = obj.get('street_postdirection', None)
        self.street_suffix = obj.get('street_suffix', None)
        self.secondary_number = obj.get('secondary_number', None)
        self.secondary_designator = obj.get('secondary_designator', None)
        self.extra_secondary_number = obj.get('extra_secondary_number', None)
        self.extra_secondary_designator = obj.get('extra_secondary_designator', None)
        self.pmb_designator = obj.get('pmb_designator', None)
        self.pmb_number = obj.get('pmb_number', None)
        self.city_name = obj.get('city_name', None)
        self.default_city_name = obj.get('default_city_name', None)
        self.state_abbreviation = obj.get('state_abbreviation', None)
        self.zipcode = obj.get('zipcode', None)
        self.plus4_code = obj.get('plus4_code', None)
        self.delivery_point = obj.get('delivery_point', None)
        self.delivery_point_check_digit = obj.get('delivery_point_check_digit', None)
