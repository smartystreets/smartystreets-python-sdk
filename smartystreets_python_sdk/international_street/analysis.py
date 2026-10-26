from .changes import Changes

class Analysis:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/international-street-api#analysis"
        """
        self.verification_status: str | None = obj.get('verification_status')
        self.address_precision: str | None = obj.get('address_precision')
        self.max_address_precision: str | None = obj.get('max_address_precision')
        self.changes: Changes = Changes(obj.get("changes", {}))
