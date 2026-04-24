import os

from smartystreets_python_sdk import BasicAuthCredentials, ClientBuilder
from smartystreets_python_sdk.us_enrichment.lookup import GeoReferenceLookup


def run():
    # We recommend storing your secret keys in environment variables instead---it's safer!
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_enrichment_api_client()

    smarty_key = "87844267"

    lookup = GeoReferenceLookup()
    freeform_lookup = GeoReferenceLookup()

    lookup.smartykey = smarty_key
    # lookup.street = "1708 Watson Way"
    # lookup.city = "Vineyard"
    # lookup.state = "UT"
    # lookup.zipcode = "84059"

    # Uncomment to narrow the response with include/exclude attributes
    # lookup.add_include_attribute('census_block')
    # lookup.add_exclude_attribute('place')

    # Uncomment to add a custom parameter
    # lookup.add_custom_parameter("parameter", "value")

    freeform_lookup.freeform = "1708 Watson Way Vineyard UT 84059"

    try:
        # Send a lookup by SmartyKey alone
        # results = client.send_geo_reference_lookup(smarty_key)
        # Or send it by address components
        results = client.send_geo_reference_lookup(lookup)
        # Or send it by freeform address
        # results = client.send_geo_reference_lookup(freeform_lookup)

        # Or run it through the generic endpoint instead
        # results = client.send_generic_lookup(smarty_key, 'geo-reference', None)
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
