import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, exceptions, Batch, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType


def run():
    # key = "Your SmartyStreets Key here"
    # hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # for client-side requests (browser/mobile), use this code:
    # key = os.environ['SMARTY_AUTH_WEB']
    # hostname = os.environ['SMARTY_WEBSITE_DOMAIN']

    # credentials = SharedCredentials(key, hostname)

    # for server-to-server requests, use this code:
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_street_api_client()
    
    batch = Batch()

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-street-api#input-fields

    batch.add(StreetLookup())
    batch[0].input_id = "24601"  # Optional ID from your system
    batch[0].addressee = "John Doe"
    batch[0].street = "1600 amphitheatre parkway"
    batch[0].street2 = "closet under the stairs"
    batch[0].secondary = "APT 2"
    batch[0].urbanization = ""  # Only applies to Puerto Rico addresses
    batch[0].lastline = "Mountain view, california"
    batch[0].candidates = 5
    batch[0].match = MatchType.INVALID  # "invalid" is the most permissive match,
                                        # this will always return at least one result even if the address is invalid.
                                        # Refer to the documentation for additional Match Strategy options.

    # Uncomment the below line to add a custom parameter
    # batch[0].add_custom_parameter("parameter", "value")

    batch.add(StreetLookup("1 Rosedale, Baltimore, Maryland"))  # Freeform addresses work too.
    batch[1].candidates = 10  # Allows up to ten possible matches to be returned (default is 1).

    batch.add(StreetLookup("123 Bogus Street, Pretend Lake, Oklahoma"))

    batch.add(StreetLookup())
    batch[3].input_id = "8675309"
    batch[3].street = "1 Infinite Loop"
    batch[3].zipcode = "95014"  # You can just input the street and ZIP if you want.
    batch[3].candidates = 1

    assert len(batch) == 4

    try:
        client.send_batch(batch)
    except exceptions.SmartyException as err:
        print(err)
        return

    for i, lookup in enumerate(batch):
        candidates = lookup.result

        if len(candidates) == 0:
            print("Address {} is invalid.\n".format(i))
            continue

        print("Address {} has at least one candidate.".format(i))
        print("If the match parameter is set to STRICT, the address is valid.")
        print("Otherwise, check the Analysis output fields to see if the address is valid.\n")

        for candidate in candidates:
            components = candidate.components
            metadata = candidate.metadata

            print("\nCandidate {} : ".format(candidate.candidate_index))
            print("Delivery line 1: {}".format(candidate.delivery_line_1))
            print("Last line:       {}".format(candidate.last_line))
            print("ZIP Code:        {}-{}".format(components.zipcode, components.plus4_code))
            print("County:          {}".format(metadata.county_name))
            print("Latitude:        {}".format(metadata.latitude))
            print("Longitude:       {}".format(metadata.longitude))
        print("")


if __name__ == "__main__":
    run()
