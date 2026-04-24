import os

from smartystreets_python_sdk import BasicAuthCredentials, ClientBuilder
from smartystreets_python_sdk.us_enrichment.lookup import Lookup as EnrichmentLookup


def run():
    # We recommend storing your secret keys in environment variables instead---it's safer!
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_enrichment_api_client()

    # send_generic_lookup routes a Lookup to any dataset/dataSubset that the
    # Enrichment API exposes, including new endpoints that may not yet have a
    # dedicated helper on the client.
    smarty_key = "87844267"
    dataset = "property"
    data_subset = "principal"

    lookup = EnrichmentLookup()
    freeform_lookup = EnrichmentLookup()

    lookup.smartykey = smarty_key
    # lookup.street = "1708 Watson Way"
    # lookup.city = "Vineyard"
    # lookup.state = "UT"
    # lookup.zipcode = "84059"
    lookup.features = "financial"

    # Uncomment to narrow the response with include/exclude attributes
    # lookup.add_include_attribute('assessed_value')
    # lookup.add_exclude_attribute('tax_billed_amount')

    freeform_lookup.freeform = "1708 Watson Way Vineyard UT 84059"

    try:
        # Send a lookup by SmartyKey alone
        # results = client.send_generic_lookup(smarty_key, dataset, data_subset)
        # Or send it by address components
        results = client.send_generic_lookup(lookup, dataset, data_subset)
        # Or send it by freeform address
        # results = client.send_generic_lookup(freeform_lookup, dataset, data_subset)
    except Exception as err:
        print(err)
        return

    if not results:
        print("No results found. This means the SmartyKey or address is likely not valid, or does not have data in this dataset")
        return

    top_result = results[0]

    print("Here is your result!")
    print(top_result)


if __name__ == "__main__":
    run()
