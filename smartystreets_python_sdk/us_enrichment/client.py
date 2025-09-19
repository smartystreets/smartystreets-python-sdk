from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from .lookup import FinancialLookup, PrincipalLookup, GeoReferenceLookup, RiskLookup, SecondaryLookup, SecondaryCountLookup, Lookup
from .response import Response


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_enrichment_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send_property_financial_lookup(self, lookup):
        if isinstance(lookup, str):
            l = FinancialLookup(lookup)
            send_lookup(self, l)
            return l.result
        else:
            lookup.dataset = 'property'
            lookup.dataSubset = 'financial'
            send_lookup(self, lookup)
            return lookup.result
        
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


def send_lookup(client: Client, lookup):
    """
    Sends a Lookup object to the US Enrichment API and stores the result in the Lookup's result field.
    """
    if lookup is None or (lookup.smartykey is None and lookup.street is None and lookup.freeform is None):
        raise SmartyException('Client.send() requires a Lookup with either the "smartykey", "street, or "freeform" field set as a string')

    request = build_request(lookup)

    response = client.sender.send(request)
    if response.error:
        raise response.error

    response = client.serializer.deserialize(response.payload)
    result = []
    for candidate in response:
        result.append(Response(candidate))
    lookup.result = result
    return result


def build_request(lookup):
    request = Request()
    if lookup.smartykey != None:
        if lookup.dataSubset == None:
            request.url_components = lookup.smartykey + "/" + lookup.dataset
            request.parameters = remap_keys(lookup)
            return request
    
        request.url_components = lookup.smartykey + "/" + lookup.dataset + "/" + lookup.dataSubset
        request.parameters = remap_keys(lookup)

        return request
    else:
        if lookup.dataSubset == None:
            request.url_components = 'search/' + lookup.dataset
            request.parameters = remap_keys(lookup)
            return request
    
        request.url_components = 'search/' + lookup.dataset + "/" + lookup.dataSubset

        request.parameters = remap_keys(lookup)
        return request
    
def remap_keys(lookup):
    converted_lookup = {}

    if (lookup.freeform != None):
        add_field(converted_lookup, 'freeform', lookup.freeform)
    if (lookup.street != None):
        add_field(converted_lookup, 'street', lookup.street)
    if (lookup.city != None):
        add_field(converted_lookup, 'city', lookup.city)
    if (lookup.state != None):
        add_field(converted_lookup, 'state', lookup.state)
    if (lookup.zipcode != None):
        add_field(converted_lookup, 'zipcode', lookup.zipcode)
    if (lookup.include_array != None):
        add_field(converted_lookup, 'include', build_filter_string(lookup.include_array))
    if (lookup.exclude_array != None):
        add_field(converted_lookup, 'exclude', build_filter_string(lookup.exclude_array))
    if (lookup.features != None):
        add_field(converted_lookup, 'features', lookup.features)


    for parameter in lookup.custom_parameter_array:
        add_field(converted_lookup, parameter, lookup.custom_parameter_array[parameter])

    return converted_lookup


def add_field(converted_lookup, key, value):
    if value:
        converted_lookup[key] = value

def build_filter_string(filter_list):
    return ','.join(filter_list or []) or None
