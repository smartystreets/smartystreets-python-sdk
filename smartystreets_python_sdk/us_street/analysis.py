class Analysis:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-street-api#analysis"
        """
        self.dpv_match_code = obj.get('dpv_match_code', None)
        self.dpv_footnotes = obj.get('dpv_footnotes', None)
        self.cmra = obj.get('dpv_cmra', None)
        self.vacant = obj.get('dpv_vacant', None)
        self.active = obj.get('active', None)
        self.dpv_no_stat = obj.get('dpv_no_stat', None)
        self.is_ews_match = obj.get('ews_match', DeprecationWarning)
        self.footnotes = obj.get('footnotes', None)
        self.lacs_link_code = obj.get('lacslink_code', None)
        self.lacs_link_indicator = obj.get('lacslink_indicator', None)
        self.is_suite_link_match = obj.get('suitelink_match', None)
        self.enhanced_match = obj.get('enhanced_match', None)
