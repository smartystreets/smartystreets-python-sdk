import os

from smartystreets_python_sdk import StaticCredentials, exceptions, Batch
from smartystreets_python_sdk.us_street import ClientBuilder, Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build()
    batch = Batch()

    batch.add(Lookup())
    batch[0].street = "1600 amphitheatre parkway"
    batch[0].city = "Mountain view"
    batch[0].state = "california"

    batch.add(Lookup("1 Rosedale, Baltimore, Maryland"))  # Freeform addresses work too.
    batch[1].candidates = 10  # Allows up to ten possible matches to be returned (default is 1).

    batch.add(Lookup("123 Bogus Street, Pretend Lake, Oklahoma"))

    batch.add(Lookup())
    batch[3].street = "1 Infinite Loop"
    batch[3].zipcode = "95014"  # You can just input the street and ZIP if you want.

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

        print("Address {} is valid. (There is at least one candidate)".format(i))

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
