from .match_info import MatchInfo

class ComponentAnalysis:
    def __init__(self, obj):
        """
        This class contains detailed match information for each component of an address.
        """
        self.primary_number = MatchInfo(obj['primary_number']) if 'primary_number' in obj else None
        self.street_predirection = MatchInfo(obj['street_predirection']) if 'street_predirection' in obj else None
        self.street_name = MatchInfo(obj['street_name']) if 'street_name' in obj else None
        self.street_postdirection = MatchInfo(obj['street_postdirection']) if 'street_postdirection' in obj else None
        self.street_suffix = MatchInfo(obj['street_suffix']) if 'street_suffix' in obj else None
        self.secondary_number = MatchInfo(obj['secondary_number']) if 'secondary_number' in obj else None
        self.secondary_designator = MatchInfo(obj['secondary_designator']) if 'secondary_designator' in obj else None
        self.extra_secondary_number = MatchInfo(obj['extra_secondary_number']) if 'extra_secondary_number' in obj else None
        self.extra_secondary_designator = MatchInfo(obj['extra_secondary_designator']) if 'extra_secondary_designator' in obj else None
        self.city_name = MatchInfo(obj['city_name']) if 'city_name' in obj else None
        self.state_abbreviation = MatchInfo(obj['state_abbreviation']) if 'state_abbreviation' in obj else None
        self.zipcode = MatchInfo(obj['zipcode']) if 'zipcode' in obj else None
        self.plus4_code = MatchInfo(obj['plus4_code']) if 'plus4_code' in obj else None
        self.urbanization = MatchInfo(obj['urbanization']) if 'urbanization' in obj else None

    def to_dict(self):
        result = {
            'primary_number': self.primary_number.to_dict() if self.primary_number else None,
            'street_predirection': self.street_predirection.to_dict() if self.street_predirection else None,
            'street_name': self.street_name.to_dict() if self.street_name else None,
            'street_postdirection': self.street_postdirection.to_dict() if self.street_postdirection else None,
            'street_suffix': self.street_suffix.to_dict() if self.street_suffix else None,
            'secondary_number': self.secondary_number.to_dict() if self.secondary_number else None,
            'secondary_designator': self.secondary_designator.to_dict() if self.secondary_designator else None,
            'extra_secondary_number': self.extra_secondary_number.to_dict() if self.extra_secondary_number else None,
            'extra_secondary_designator': self.extra_secondary_designator.to_dict() if self.extra_secondary_designator else None,
            'city_name': self.city_name.to_dict() if self.city_name else None,
            'state_abbreviation': self.state_abbreviation.to_dict() if self.state_abbreviation else None,
            'zipcode': self.zipcode.to_dict() if self.zipcode else None,
            'plus4_code': self.plus4_code.to_dict() if self.plus4_code else None,
            'urbanization': self.urbanization.to_dict() if self.urbanization else None,
        }
        return {k: v for k, v in result.items() if v is not None}