propertyDataset = "property"
financialDataSubset = "financial"
principalDataSubset = "principal"
geoReferenceDataset = "geo-reference"
secondaryDataset = "secondary"
countDataSubset = "count"
noneDataSubset = None

class Lookup:
    def __init__(self, smartykey = None, dataset = None, dataSubset = None, freeform = None, street = None, city = None, state = None, zipcode = None):
        self.smartykey = smartykey
        self.dataset = dataset
        self.dataSubset = dataSubset
        self.freeform = freeform
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.result = []

class FinancialLookup(Lookup):
    def __init__(self, smartykey = None):
        super().__init__(smartykey, propertyDataset, financialDataSubset)

class PrincipalLookup(Lookup):
    def __init__(self, smartykey = None):
        super().__init__(smartykey, propertyDataset, principalDataSubset)

class GeoReferenceLookup(Lookup):
    def __init__(self, smartykey = None):
        super().__init__(smartykey, geoReferenceDataset, noneDataSubset)

class SecondaryLookup(Lookup):
    def __init__(self, smartykey = None):
        super().__init__(smartykey, secondaryDataset, noneDataSubset)

class SecondaryCountLookup(Lookup):
    def __init__(self, smartykey = None):
        super().__init__(smartykey, secondaryDataset, countDataSubset)