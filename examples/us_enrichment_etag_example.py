import os

from smartystreets_python_sdk import BasicAuthCredentials, ClientBuilder
from smartystreets_python_sdk.exceptions import NotModifiedError
from smartystreets_python_sdk.us_enrichment import BusinessDetailLookup, BusinessLookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_enrichment_api_client()

    smarty_key = "1962995076"

    business_id = exercise_summary_etag(client, smarty_key)
    if business_id is None:
        return

    exercise_detail_etag(client, business_id)


def exercise_summary_etag(client, smarty_key):
    print("=== Business.Summary ETag round trip ===")

    first = BusinessLookup(smarty_key)
    try:
        client.send_business_lookup(first)
    except Exception as ex:
        print("  Initial Summary call failed: {}".format(ex))
        return None

    initial_results = first.result
    captured_etag = first.response_etag
    print("  Call 1 (no Etag): captured Etag={}, results={}".format(
        display(captured_etag), len(initial_results or [])))

    if not captured_etag:
        print("  Server did not return an Etag header; skipping conditional calls.")
        return first_business_id(initial_results)

    second = BusinessLookup(smarty_key)
    second.request_etag = captured_etag
    try:
        client.send_business_lookup(second)
        print("  Call 2 (matching Etag): 200 — server did NOT honor the conditional. Results={}, Etag={}".format(
            len(second.result or []), display(second.response_etag)))
    except NotModifiedError as ex:
        print("  Call 2 (matching Etag): 304 NotModifiedError — caller treats this as cache-valid. Refreshed Etag={}".format(
            display(ex.response_etag)))
    except Exception as ex:
        print("  Call 2 unexpected failure: {}: {}".format(type(ex).__name__, ex))
        return None

    third = BusinessLookup(smarty_key)
    third.request_etag = captured_etag + "X"
    try:
        client.send_business_lookup(third)
        print("  Call 3 (mutated Etag): 200 as expected. Results={}, Etag={}".format(
            len(third.result or []), display(third.response_etag)))
    except NotModifiedError:
        print("  Call 3 (mutated Etag): 304 — UNEXPECTED. Server treated a different Etag as matching.")
    except Exception as ex:
        print("  Call 3 unexpected failure: {}: {}".format(type(ex).__name__, ex))

    return first_business_id(initial_results)


def exercise_detail_etag(client, business_id):
    print()
    print("=== Business.Detail ETag round trip (businessId: {}) ===".format(business_id))

    first = BusinessDetailLookup(business_id)
    try:
        client.send_business_detail_lookup(first)
    except Exception as ex:
        print("  Initial Detail call failed: {}".format(ex))
        return

    initial = first.result
    captured_etag = first.response_etag
    initial_id = initial.business_id if initial is not None else "<null>"
    print("  Call 1 (no Etag): captured Etag={}, businessId={}".format(
        display(captured_etag), initial_id))

    if not captured_etag:
        print("  Server did not return an Etag header; skipping conditional calls.")
        return

    second = BusinessDetailLookup(business_id)
    second.request_etag = captured_etag
    try:
        client.send_business_detail_lookup(second)
        second_id = second.result.business_id if second.result is not None else "<null>"
        print("  Call 2 (matching Etag): 200 — server did NOT honor the conditional. businessId={}, Etag={}".format(
            second_id, display(second.response_etag)))
    except NotModifiedError as ex:
        print("  Call 2 (matching Etag): 304 NotModifiedError — caller treats this as cache-valid. Refreshed Etag={}".format(
            display(ex.response_etag)))
    except Exception as ex:
        print("  Call 2 unexpected failure: {}: {}".format(type(ex).__name__, ex))
        return

    third = BusinessDetailLookup(business_id)
    third.request_etag = captured_etag + "X"
    try:
        client.send_business_detail_lookup(third)
        third_id = third.result.business_id if third.result is not None else "<null>"
        print("  Call 3 (mutated Etag): 200 as expected. businessId={}, Etag={}".format(
            third_id, display(third.response_etag)))
    except NotModifiedError:
        print("  Call 3 (mutated Etag): 304 — UNEXPECTED. Server treated a different Etag as matching.")
    except Exception as ex:
        print("  Call 3 unexpected failure: {}: {}".format(type(ex).__name__, ex))


def first_business_id(results):
    if not results:
        return None
    businesses = results[0].businesses
    if not businesses:
        return None
    return businesses[0].business_id


def display(s):
    return "<none>" if not s else s


if __name__ == "__main__":
    run()
