import os

from smartystreets_python_sdk import BasicAuthCredentials, ClientBuilder
from smartystreets_python_sdk.us_enrichment import BusinessLookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_enrichment_api_client()

    # Business summary SEARCH path: no smartykey, set freeform (+ optional city)
    # and business_name to narrow the search to a specific business.
    lookup = BusinessLookup()
    lookup.freeform = "1600 amphitheatre pkwy mountain view ca"
    lookup.business_name = "Google"

    try:
        summary_results = client.send_business_lookup(lookup)
    except Exception as err:
        print(err)
        return

    if not summary_results:
        print("No matching businesses returned")
        return

    summary = summary_results[0]
    if not summary.businesses:
        print("No business tenants matched the search")
        return

    print("Matching businesses for business_name '{}':".format(lookup.business_name))
    for biz in summary.businesses:
        print("  - {} (ID: {})".format(biz.company_name, biz.business_id))

    first = summary.businesses[0]
    print("\nFetching details for business: {} (ID: {})".format(first.company_name, first.business_id))

    try:
        detail_result = client.send_business_detail_lookup(first.business_id)
    except Exception as err:
        print(err)
        return

    if detail_result is None:
        print("\nNo detail result returned")
        return

    print("\nDetail result:")
    print_result(detail_result)


def print_result(obj):
    for key, value in vars(obj).items():
        if value is None:
            continue
        if key == 'attributes':
            print_result(value)
            continue
        print("{}: {}".format(key, value))
    print()


if __name__ == "__main__":
    run()
