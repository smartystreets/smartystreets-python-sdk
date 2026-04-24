class BusinessEntry:
    def __init__(self, obj):
        self.company_name = obj.get('company_name', None)
        self.business_id = obj.get('business_id', None)


class BusinessSummaryResponse:
    def __init__(self, obj):
        self.smarty_key = obj.get('smarty_key', None)
        self.data_set_name = obj.get('data_set_name', None)
        businesses = obj.get('businesses', None)
        if businesses is None:
            self.businesses = []
        else:
            self.businesses = [BusinessEntry(b) for b in businesses]
