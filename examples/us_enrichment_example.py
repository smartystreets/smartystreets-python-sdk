import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, exceptions, ClientBuilder


# from smartystreets_python_sdk.us_enrichment import

def run():
    # key = "Your SmartyStreets Key here"
    # hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # for client-side requests (browser/mobile), use this code:
    key = os.environ['SMARTY_AUTH_WEB']
    hostname = os.environ['SMARTY_WEBSITE_DOMAIN']

    credentials = SharedCredentials(key, hostname)

    # for server-to-server requests, use this code:
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']
    #
    # credentials = StaticCredentials(auth_id, auth_token)

    # The appropriate license values to be used for your subscriptions
    # can be found on the Subscriptions page of the account dashboard.
    # https://www.smartystreets.com/docs/cloud/licensing
    client = ClientBuilder(credentials).with_licenses(["us-property-data-principal-cloud"]).build_us_enrichment_api_client()
    # client = ClientBuilder(credentials).with_custom_header({'User-Agent': 'smartystreets (python@0.0.0)', 'Content-Type': 'application/json'}).build_us_enrichment_api_client()
    # client = ClientBuilder(credentials).with_http_proxy('localhost:8080', 'user', 'password').build_us_street_api_client()
    # Uncomment the line above to try it with a proxy instead

    smarty_key = "1682393594"
    try:
        results = client.send_property_principal_lookup(smarty_key)
        # results = client.send_generic_lookup(smarty_key, 'property', 'principal')
        # Uncomment the line above to try it as a generic lookup instead
    except Exception as err:
        print(err)
        return

    if not results:
        print("No results found. This means the Smartykey is likely not valid.")
        return

    top_result = results[0]

    print("Here is your result!")
    print(top_result)


if __name__ == "__main__":
    run()
