import os

from smartystreets_python_sdk import BasicAuthCredentials, ClientBuilder


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_enrichment_api_client()

    smarty_key = "1962995076"

    try:
        summary_results = client.send_business_lookup(smarty_key)
    except Exception as err:
        print(err)
        return

    if not summary_results:
        print("No response returned for SmartyKey {}".format(smarty_key))
        return

    summary = summary_results[0]
    if not summary.businesses:
        print("SmartyKey {} has no business tenants".format(smarty_key))
        return

    print("Summary results for SmartyKey: {}".format(smarty_key))
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
