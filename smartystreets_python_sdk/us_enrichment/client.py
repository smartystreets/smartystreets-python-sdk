from urllib.parse import quote

from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from .business import BusinessSummaryResponse, BusinessDetailResponse
from .lookup import (
    BusinessDetailLookup,
    BusinessLookup,
    GeoReferenceLookup,
    Lookup,
    PrincipalLookup,
    RiskLookup,
    SecondaryCountLookup,
    SecondaryLookup,
)
from .response import Response


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_enrichment_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send_property_principal_lookup(self, lookup):
        if isinstance(lookup, str):
            l = PrincipalLookup(lookup)
            send_lookup(self, l)
            return l.result
        else:
            lookup.dataset = 'property'
            lookup.dataSubset = 'principal'
            send_lookup(self, lookup)
            return lookup.result

    def send_geo_reference_lookup(self, lookup):
        if isinstance(lookup, str):
            l = GeoReferenceLookup(lookup)
            send_lookup(self, l)
            return l.result
        else:
            lookup.dataset = 'geo-reference'
            lookup.dataSubset = None
            send_lookup(self, lookup)
            return lookup.result

    def send_risk_lookup(self, lookup):
        if isinstance(lookup, str):
            l = RiskLookup(lookup)
            send_lookup(self, l)
            return l.result
        else:
            lookup.dataset = 'risk'
            lookup.dataSubset = None
            send_lookup(self, lookup)
            return lookup.result

    def send_secondary_lookup(self, lookup):
        if isinstance(lookup, str):
            l = SecondaryLookup(lookup)
            send_lookup(self, l)
            return l.result
        else:
            lookup.dataset = 'secondary'
            lookup.dataSubset = None
            send_lookup(self, lookup)
            return lookup.result

    def send_secondary_count_lookup(self, lookup):
        if isinstance(lookup, str):
            l = SecondaryCountLookup(lookup)
            send_lookup(self, l)
            return l.result
        else:
            lookup.dataset = 'secondary'
            lookup.dataSubset = 'count'
            send_lookup(self, lookup)
            return lookup.result

    def send_generic_lookup(self, lookup, dataset, dataSubset):
        if isinstance(lookup, str):
            l = Lookup(lookup, dataset, dataSubset)
            send_lookup(self, l)
            return l.result
        else:
            lookup.dataset = dataset
            lookup.dataSubset = dataSubset
            send_lookup(self, lookup)
            return lookup.result

    def send_business_lookup(self, lookup):
        if isinstance(lookup, str):
            l = BusinessLookup(lookup)
            send_lookup(self, l, BusinessSummaryResponse)
            return l.result
        else:
            lookup.dataset = 'business'
            lookup.dataSubset = None
            send_lookup(self, lookup, BusinessSummaryResponse)
            return lookup.result

    def send_business_detail_lookup(self, lookup):
        if isinstance(lookup, str):
            l = BusinessDetailLookup(lookup)
            send_business_detail_lookup(self, l)
            return l.result
        else:
            send_business_detail_lookup(self, lookup)
            return lookup.result


def send_lookup(client: Client, lookup, response_class=Response):
    """
    Sends a Lookup object to the US Enrichment API and stores the result in the Lookup's result field.
    """
    if lookup is None or (
        _is_blank(getattr(lookup, 'smartykey', None))
        and _is_blank(getattr(lookup, 'street', None))
        and _is_blank(getattr(lookup, 'freeform', None))
    ):
        raise SmartyException("Lookup requires one of 'smartykey', 'street', or 'freeform' to be set")

    request = build_request(lookup)
    raw = _dispatch(client, request, lookup)
    lookup.result = [response_class(candidate) for candidate in raw]
    return lookup.result


def send_business_detail_lookup(client: Client, lookup):
    if lookup is None or _is_blank(getattr(lookup, 'business_id', None)):
        raise SmartyException("BusinessDetailLookup requires a non-empty 'business_id'")

    request = Request()
    request.url_components = 'business/' + quote(lookup.business_id, safe='')
    request.parameters = _common_parameters(lookup)
    _apply_etag_header(request, lookup)

    raw = _dispatch(client, request, lookup)
    if not raw:
        lookup.result = None
    elif len(raw) > 1:
        raise SmartyException(
            "business detail response contained {} results; expected at most 1".format(len(raw))
        )
    else:
        lookup.result = BusinessDetailResponse(raw[0])
    return lookup.result


def build_request(lookup):
    request = Request()
    request.url_components = _url_components(lookup)
    request.parameters = _address_parameters(lookup)
    request.parameters.update(_common_parameters(lookup))
    _apply_etag_header(request, lookup)
    return request


def _url_components(lookup):
    if lookup.smartykey is not None:
        base = lookup.smartykey + "/" + lookup.dataset
    else:
        base = 'search/' + lookup.dataset
    if lookup.dataSubset is None:
        return base
    return base + "/" + lookup.dataSubset


def _address_parameters(lookup):
    params = {}
    for key in ('freeform', 'street', 'city', 'state', 'zipcode', 'features'):
        value = getattr(lookup, key, None)
        if value:
            params[key] = value
    return params


def _common_parameters(lookup):
    params = {}
    if lookup.include_array:
        params['include'] = ','.join(lookup.include_array)
    if lookup.exclude_array:
        params['exclude'] = ','.join(lookup.exclude_array)
    for key, value in lookup.custom_parameter_array.items():
        params[key] = value
    return params


def _apply_etag_header(request, lookup):
    if lookup.request_etag is not None:
        request.headers['Etag'] = lookup.request_etag


def _dispatch(client, request, lookup):
    response = client.sender.send(request)
    lookup.response_etag = response.find_header('etag')
    if response.error:
        raise response.error
    raw = client.serializer.deserialize(response.payload)
    return raw or []


def _is_blank(value):
    return value is None or (isinstance(value, str) and value.strip() == '')
