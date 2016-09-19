import os
from smartystreets_python_sdk import StaticCredentials
from smartystreets_python_sdk.us_street import ClientBuilder, Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build()

    lookup = Lookup()
    lookup.street = "1600 Amphitheatre Pkwy"
    lookup.city = "Mountain View"
    lookup.state = "CA"

    client.send_lookup(lookup)

    result = lookup.result

    if not result:
        print "No candidates. This means the address is not valid."
        return

    first_candidate = result[0]

    print "Address is valid. (There is at least one candidate)\n"
    print "ZIP Code: " + first_candidate.components.zipcode
    print "County: " + first_candidate.metadata.county_name
    print "Latitude: {}".format(first_candidate.metadata.latitude)
    print "Longitude: {}".format(first_candidate.metadata.longitude)

if __name__ == "__main__":
    run()
