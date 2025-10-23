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