import os

from smartystreets_python_sdk import BasicAuthCredentials, ClientBuilder
from smartystreets_python_sdk.us_enrichment.lookup import SecondaryLookup


def run():
    # We recommend storing your secret keys in environment variables instead---it's safer!
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_enrichment_api_client()

    # 875 N Michigan Ave, Chicago IL — a multi-unit tower with many secondary addresses
    smarty_key = "1788864303"

    lookup = SecondaryLookup()
    freeform_lookup = SecondaryLookup()

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
        # results = client.send_secondary_lookup(smarty_key)
        # Or send it by address components
        results = client.send_secondary_lookup(lookup)
        # Or send it by freeform address
        # results = client.send_secondary_lookup(freeform_lookup)

        # Or run it through the generic endpoint instead
        # results = client.send_generic_lookup(smarty_key, 'secondary', None)
    except Exception as err:
        print(err)
        return

    if not results:
        print("No results found. This address may not have any secondary (unit) addresses on file.")
        return

    top_result = results[0]

    print("Root address SmartyKey: {}".format(getattr(top_result, 'smarty_key', None)))
    print("Secondary addresses: {}".format(len(top_result.secondaries or [])))
    for secondary in (top_result.secondaries or [])[:5]:
        print("  {} {} (SmartyKey {})".format(
            secondary.secondary_designator,
            secondary.secondary_number,
            secondary.smarty_key,
        ))


if __name__ == "__main__":
    run()
