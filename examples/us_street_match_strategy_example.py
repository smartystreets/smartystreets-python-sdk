import os

from smartystreets_python_sdk import BasicAuthCredentials, exceptions, Batch, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType


def run():
    # We recommend storing your secret keys in environment variables instead---it's safer!
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_street_api_client()

    # Each address is run through all three match strategies so you can compare how
    # 'strict', 'enhanced', and 'invalid' each handle a valid, an invalid, and an
    # ambiguous address.
    #   - strict:   only returns candidates that are valid, mailable addresses.
    #   - enhanced: returns a more comprehensive dataset (requires a US Core or Rooftop license).
    #   - invalid:  most permissive; always returns at least one candidate (a best-guess standardization).
    # Documentation for input fields: https://smartystreets.com/docs/us-street-api#input-fields
    addresses = [
        ("valid (real, deliverable)",   "1600 Amphitheatre Pkwy", "Mountain View", "CA", "94043"),
        ("invalid (no such address)",   "9999 W 1150 S",          "Provo",         "UT", "84601"),
        ("ambiguous (missing ZIP/unit)", "1 Rosedale St",         "Baltimore",     "MD", ""),
    ]
    strategies = [MatchType.STRICT, MatchType.ENHANCED, MatchType.INVALID]

    batch = Batch()
    cases = []  # parallel metadata for each lookup, in the order they are added to the batch

    for label, street, city, state, zipcode in addresses:
        for strategy in strategies:
            lookup = StreetLookup()
            lookup.street = street
            lookup.city = city
            lookup.state = state
            lookup.zipcode = zipcode
            lookup.match = strategy
            lookup.candidates = 10  # allow ambiguous addresses to return more than one match
            batch.add(lookup)
            cases.append((label, "{}, {}, {}".format(street, city, state), strategy.value))

    try:
        client.send_batch(batch)
    except exceptions.SmartyException as err:
        print(err)
        return

    last_address = None
    for i, lookup in enumerate(batch):
        label, address_display, strategy = cases[i]

        if address_display != last_address:
            print("\n" + "=" * 70)
            print(" Address: {}  [{}]".format(address_display, label))
            print("=" * 70)
            last_address = address_display

        candidates = lookup.result
        print("\n--- '{}' strategy ---".format(strategy))

        if len(candidates) == 0:
            print("  0 candidates - no match returned under this strategy.")
            continue

        print("  {} candidate(s):".format(len(candidates)))
        for candidate in candidates:
            print("    [{}] {}  {}".format(candidate.candidate_index, candidate.delivery_line_1, candidate.last_line))


if __name__ == "__main__":
    run()
