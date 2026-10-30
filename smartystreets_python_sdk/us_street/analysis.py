from .component_analysis import ComponentAnalysis

class Analysis:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-street-api#analysis"
        """
        self.dpv_match_code: str | None = obj.get('dpv_match_code', None)
        self.dpv_footnotes: str | None = obj.get('dpv_footnotes', None)
        self.cmra: str | None = obj.get('dpv_cmra', None)
        self.vacant: str | None = obj.get('dpv_vacant', None)
        self.active: str | None = obj.get('active', None)
        self.dpv_no_stat: str | None = obj.get('dpv_no_stat', None)
        self.is_ews_match: bool | type[DeprecationWarning] | None = obj.get('ews_match', DeprecationWarning)
        self.footnotes: str | None = obj.get('footnotes', None)
        self.lacs_link_code: str | None = obj.get('lacslink_code', None)
        self.lacs_link_indicator: str | None = obj.get('lacslink_indicator', None)
        self.is_suite_link_match: bool | None = obj.get('suitelink_match', None)
        self.enhanced_match: str | None = obj.get('enhanced_match', None)
        components_obj = obj.get("components", None)
        self.components: ComponentAnalysis | None = ComponentAnalysis(components_obj) if components_obj else None

    def to_dict(self) -> dict:
        components_dict = self.components.to_dict() if self.components else None

        result = {
            "dpv_match_code": self.dpv_match_code,
            "dpv_footnotes": self.dpv_footnotes,
            "dpv_cmra": self.cmra,
            "dpv_vacant": self.vacant,
            "active": self.active,
            "dpv_no_stat": self.dpv_no_stat,
            "footnotes": self.footnotes,
            "lacslink_code": self.lacs_link_code,
            "lacslink_indicator": self.lacs_link_indicator,
            "suitelink_match": self.is_suite_link_match,
            "enhanced_match": self.enhanced_match,
            "components": components_dict or None
        }
        return {k: v for k, v in result.items() if v is not None}
