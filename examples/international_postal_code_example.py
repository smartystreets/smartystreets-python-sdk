import os

from smartystreets_python_sdk import BasicCredentials, ClientBuilder
from smartystreets_python_sdk.international_postal_code import Lookup


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
    
    credentials = BasicCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_international_postal_code_api_client()

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/cloud/international-postal-code-api

    lookup = Lookup()
    lookup.input_id = "ID-8675309"
    lookup.locality = "Sao Paulo"
    lookup.administrative_area = "SP"
    lookup.country = "Brazil"
    lookup.postal_code = "02516"

    candidates = client.send(lookup)  # The candidates are also stored in the lookup's 'results' field.

    print("Results:")
    print()

    for idx, candidate in enumerate(candidates):
        print("Candidate: {}".format(idx))
        
        if candidate.input_id:
            print("  input_id: {}".format(candidate.input_id))
        if candidate.country_iso_3:
            print("  country_iso_3: {}".format(candidate.country_iso_3))
        if candidate.locality:
            print("  locality: {}".format(candidate.locality))
        if candidate.dependent_locality:
            print("  dependent_locality: {}".format(candidate.dependent_locality))
        if candidate.double_dependent_locality:
            print("  double_dependent_locality: {}".format(candidate.double_dependent_locality))
        if candidate.sub_administrative_area:
            print("  sub_administrative_area: {}".format(candidate.sub_administrative_area))
        if candidate.administrative_area:
            print("  administrative_area: {}".format(candidate.administrative_area))
        if candidate.super_administrative_area:
            print("  super_administrative_area: {}".format(candidate.super_administrative_area))
        if candidate.postal_code:
            print("  postal_code: {}".format(candidate.postal_code))
        if candidate.postal_code_extra:
            print("  postal_code_extra: {}".format(candidate.postal_code_extra))
        
        print()


if __name__ == "__main__":
    run()
