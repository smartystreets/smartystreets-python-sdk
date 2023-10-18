propertyDataset = "property"
financialDataSubset = "financial"
principalDataSubset = "principal"

class Lookup:
    def __init__(self, smartykey, dataset, dataSubset):
        self.smartykey = smartykey
        self.dataset = dataset
        self.dataSubset = dataSubset
        self.result = []

class FinancialLookup(Lookup):
    def __init__(self, smartykey):
        super().__init__(smartykey, propertyDataset, financialDataSubset)

class PrincipalLookup(Lookup):
    def __init__(self, smartykey):
        super().__init__(smartykey, propertyDataset, principalDataSubset)