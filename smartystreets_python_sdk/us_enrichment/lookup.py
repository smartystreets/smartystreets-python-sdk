propertyDataset = "property"
principalDataSubset = "principal"
geoReferenceDataset = "geo-reference"
riskDataset = "risk"
secondaryDataset = "secondary"
countDataSubset = "count"
businessDataset = "business"
noneDataSubset = None


class LookupBase:
    def __init__(self):
        self.include_array = []
        self.exclude_array = []
        self.request_etag = None
        self.response_etag = None
        self.custom_parameter_array = {}

    def add_custom_parameter(self, parameter, value):
        self.custom_parameter_array[parameter] = value

    def add_include_attribute(self, attribute):
        if attribute not in self.include_array:
            self.include_array.append(attribute)

    def add_exclude_attribute(self, attribute):
        if attribute not in self.exclude_array:
            self.exclude_array.append(attribute)


class Lookup(LookupBase):
    def __init__(self, smartykey=None, dataset=None, dataSubset=None, features=None, freeform=None, street=None, city=None, state=None, zipcode=None):
        super().__init__()
        self.smartykey = smartykey
        self.dataset = dataset
        self.dataSubset = dataSubset
        self.features = features
        self.freeform = freeform
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.result = []


class PrincipalLookup(Lookup):
    def __init__(self, smartykey=None):
        super().__init__(smartykey, propertyDataset, principalDataSubset)


class GeoReferenceLookup(Lookup):
    def __init__(self, smartykey=None):
        super().__init__(smartykey, geoReferenceDataset, noneDataSubset)


class RiskLookup(Lookup):
    def __init__(self, smartykey=None):
        super().__init__(smartykey, riskDataset, noneDataSubset)


class SecondaryLookup(Lookup):
    def __init__(self, smartykey=None):
        super().__init__(smartykey, secondaryDataset, noneDataSubset)


class SecondaryCountLookup(Lookup):
    def __init__(self, smartykey=None):
        super().__init__(smartykey, secondaryDataset, countDataSubset)


class BusinessLookup(Lookup):
    def __init__(self, smartykey=None):
        super().__init__(smartykey, businessDataset, noneDataSubset)


class BusinessDetailLookup(LookupBase):
    def __init__(self, business_id=None):
        super().__init__()
        self.business_id = business_id
        self.result = None
