# -*- coding: utf-8 -*-
import os

from smartystreets_python_sdk import SharedCredentials, BasicAuthCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType


def run():
    # key = "Your SmartyStreets Key here"
    # hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # for client-side requests (browser/mobile), use this code:
    # key = os.environ['SMARTY_AUTH_WEB']
    # hostname = os.environ['SMARTY_WEBSITE_DOMAIN']
    #
    # credentials = SharedCredentials(key, hostname)

    # for server-to-server requests, use this code:
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_street_api_client()

    # client = ClientBuilder(credentials).with_custom_header({'User-Agent': 'smartystreets (python@0.0.0)', 'Content-Type': 'application/json'}).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_http_proxy('localhost:8080', 'user', 'password').build_us_street_api_client()
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
    lookup.match = MatchType.INVALID  # "invalid" is the most permissive match,
                                      # this will always return at least one result even if the address is invalid.
                                      # Refer to the documentation for additional Match Strategy options.

    # Uncomment the below line to add a custom parameter
    # lookup.add_custom_parameter("parameter", "value")

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

    print("There is at least one candidate.")
    print("If the match parameter is set to STRICT, the address is valid.")
    print("Otherwise, check the Analysis output fields to see if the address is valid.\n")
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
