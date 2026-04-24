import os

from smartystreets_python_sdk import BasicAuthCredentials, ClientBuilder
from smartystreets_python_sdk.us_enrichment.lookup import SecondaryCountLookup


def run():
    # We recommend storing your secret keys in environment variables instead---it's safer!
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_enrichment_api_client()

    # 875 N Michigan Ave, Chicago IL — a multi-unit tower with many secondary addresses
    smarty_key = "1788864303"

    lookup = SecondaryCountLookup()
    freeform_lookup = SecondaryCountLookup()

    lookup.smartykey = smarty_key
    # lookup.street = "875 N Michigan Ave"
    # lookup.city = "Chicago"
    # lookup.state = "IL"
    # lookup.zipcode = "60611"

    # Uncomment to add a custom parameter
    # lookup.add_custom_parameter("parameter", "value")

    freeform_lookup.freeform = "875 N Michigan Ave Chicago IL 60611"

    try:
        # Send a lookup by SmartyKey alone
        # results = client.send_secondary_count_lookup(smarty_key)
        # Or send it by address components
        results = client.send_secondary_count_lookup(lookup)
        # Or send it by freeform address
        # results = client.send_secondary_count_lookup(freeform_lookup)

        # Or run it through the generic endpoint instead
        # results = client.send_generic_lookup(smarty_key, 'secondary', 'count')
    except Exception as err:
        print(err)
        return

    if not results:
        print("No results found. This address may not have any secondary (unit) addresses on file.")
        return

    top_result = results[0]
    print("SmartyKey {} has {} secondary address(es) on file.".format(
        getattr(top_result, 'smarty_key', smarty_key),
        getattr(top_result, 'count', 0),
    ))


if __name__ == "__main__":
    run()
