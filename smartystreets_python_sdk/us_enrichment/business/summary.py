class BusinessEntry:
    def __init__(self, obj: dict) -> None:
        self.company_name: str | None = obj.get('company_name', None)
        self.business_id: str | None = obj.get('business_id', None)


class BusinessSummaryResponse:
    def __init__(self, obj: dict) -> None:
        self.smarty_key: str | None = obj.get('smarty_key', None)
        self.data_set_name: str | None = obj.get('data_set_name', None)
        businesses: list[dict] | None = obj.get('businesses', None)
        if businesses is None:
            self.businesses: list[BusinessEntry] = []
        else:
            self.businesses = [BusinessEntry(b) for b in businesses]
