from typing import Any

from .business import BusinessDetailResponse

propertyDataset = "property"
principalDataSubset = "principal"
geoReferenceDataset = "geo-reference"
secondaryDataset = "secondary"
countDataSubset = "count"
businessDataset = "business"
noneDataSubset = None


class LookupBase:
    def __init__(self) -> None:
        self.include_array: list[str] = []
        self.exclude_array: list[str] = []
        self.request_etag: str | None = None
        self.response_etag: str | None = None
        self.custom_parameter_array: dict[str, Any] = {}

    def add_custom_parameter(self, parameter: str, value: Any) -> None:
        self.custom_parameter_array[parameter] = value

    def add_include_attribute(self, attribute: str) -> None:
        if attribute not in self.include_array:
            self.include_array.append(attribute)

    def add_exclude_attribute(self, attribute: str) -> None:
        if attribute not in self.exclude_array:
            self.exclude_array.append(attribute)


class Lookup(LookupBase):
    def __init__(self, smartykey: str | None = None, dataset: str | None = None, dataSubset: str | None = None,
                 features: str | None = None, freeform: str | None = None, street: str | None = None,
                 city: str | None = None, state: str | None = None, zipcode: str | None = None,
                 business_name: str | None = None) -> None:
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
        self.result: list[Any] = []
        self.business_name = business_name


class PrincipalLookup(Lookup):
    def __init__(self, smartykey: str | None = None) -> None:
        super().__init__(smartykey, propertyDataset, principalDataSubset)


class GeoReferenceLookup(Lookup):
    def __init__(self, smartykey: str | None = None) -> None:
        super().__init__(smartykey, geoReferenceDataset, noneDataSubset)


class SecondaryLookup(Lookup):
    def __init__(self, smartykey: str | None = None) -> None:
        super().__init__(smartykey, secondaryDataset, noneDataSubset)


class SecondaryCountLookup(Lookup):
    def __init__(self, smartykey: str | None = None) -> None:
        super().__init__(smartykey, secondaryDataset, countDataSubset)


class BusinessLookup(Lookup):
    def __init__(self, smartykey: str | None = None) -> None:
        super().__init__(smartykey, businessDataset, noneDataSubset)


class BusinessDetailLookup(LookupBase):
    def __init__(self, business_id: str | None = None) -> None:
        super().__init__()
        self.business_id = business_id
        self.result: BusinessDetailResponse | None = None
