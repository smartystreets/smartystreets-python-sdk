import os

import smartystreets_python_sdk as smarty
from smartystreets_python_sdk import StaticCredentials
from smartystreets_python_sdk.us_street import ClientBuilder, Batch, Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = smarty.StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build()
    batch = Batch()
    addresses = []

    addresses.append(Lookup())
    addresses[0].street = "1600 amphitheatre parkway"
    addresses[0].city = "Mountain view"
    addresses[0].state = "california"

    addresses.append(Lookup("1 Rosedale, Baltimore, Maryland")) # Freeform addresses work too.
    addresses[1].candidates = 10  # Allows up to ten possible matches to be returned (default is 1).

    addresses.append(Lookup("123 Bogus Street, Pretend Lake, Oklahoma"))

    addresses.append(Lookup())
    addresses[3].street = "1 Infinite Loop"
    addresses[3].zipcode = "95014"  # You can just input the street and ZIP if you want.

    for address in addresses:
        batch.add(address)

    assert batch.size() == 4

    client.send_batch(batch)

    for i in range(0, batch.size()):
        candidates = addresses[i].result

        if len(candidates) == 0:
            print("Address {} is invalid.\n".format(i))
            continue

        print("Address {} is valid. (There is at least one candidate)".format(i))

        for candidate in candidates:
            components = candidate['components']
            metadata = candidate['metadata']

            print("\nCandidate {} : ".format(candidate['candidate_index']))
            print("Delivery line 1: {}".format(candidate['delivery_line_1']))
            print("Last line:       {}".format(candidate['last_line']))
            print("ZIP Code:        {}-{}".format(components['zipcode'], components['plus4_code']))
            print("County:          {}".format(metadata['county_name']))
            print("Latitude:        {}".format(metadata['latitude']))
            print("Longitude:       {}".format(metadata['longitude']))
        print ""


if __name__ == "__main__":
    run()
