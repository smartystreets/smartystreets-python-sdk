import os

from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    # The appropriate license values to be used for you subscriptions
    # can be found on the Subscriptions page of the account dashboard.
    # https://www.smartystreets.com/docs/cloud/licensing
    client = ClientBuilder(credentials).with_licenses("us-standard-cloud").build_us_street_api_client()
    # client = ClientBuilder(credentials).with_custom_header({'User-Agent': 'smartystreets (python@0.0.0)', 'Content-Type': 'application/json'}).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_proxy('localhost:8080', 'user', 'password').build_us_street_api_client()
    # Uncomment the line above to try it with a proxy instead

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-street-api#input-fields

    lookup = StreetLookup()
    lookup.input_id = "24601"  # Optional ID from your system
    lookup.addressee = "John Doe"
    lookup.street = "1600 Amphitheatre Pkwy"
    lookup.street2 = "closet under the stairs"
    lookup.secondary = "APT 2"
    lookup.urbanization = ""  # Only applies to Puerto Rico addresses
    lookup.city = "Mountain View"
    lookup.state = "CA"
    lookup.zipcode = "94043"
    lookup.candidates = 3
    lookup.match = "invalid"  # "invalid" is the most permissive match,
                              # this will always return at least one result even if the address is invalid.
                              # Refer to the documentation for additional Match Strategy options.

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result

    if not result:
        print("No candidates. This means the address is not valid.")
        return

    first_candidate = result[0]

    print("Address is valid. (There is at least one candidate)\n")
    print("ZIP Code: " + first_candidate.components.zipcode)
    print("County: " + first_candidate.metadata.county_name)
    print("Latitude: {}".format(first_candidate.metadata.latitude))
    print("Longitude: {}".format(first_candidate.metadata.longitude))
    # print("Precision: {}".format(first_candidate.metadata.precision))    
    # print("Residential: {}".format(first_candidate.metadata.rdi))
    # print("Vacant: {}".format(first_candidate.analysis.dpv_vacant))
    # Complete list of output fields is available here:  https://smartystreets.com/docs/cloud/us-street-api#http-response-output


if __name__ == "__main__":
    run()
