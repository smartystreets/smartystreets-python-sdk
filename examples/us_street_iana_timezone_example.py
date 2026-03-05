# -*- coding: utf-8 -*-
import os

from smartystreets_python_sdk import BasicAuthCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)

    client = ( ClientBuilder(credentials)
        .with_feature_iana_time_zone()
        .build_us_street_api_client()
    )

    lookup = StreetLookup()
    lookup.street = "1 Rosedale"
    lookup.city = "Baltimore"
    lookup.state = "MD"
    lookup.zipcode = "21229"
    lookup.match = MatchType.ENHANCED

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
    metadata = first_candidate.metadata

    print("Standard Timezone Fields:")
    print("  Time Zone:  {}".format(metadata.time_zone))
    print("  UTC Offset: {}".format(metadata.utc_offset))
    print("  Obeys DST:  {}".format(metadata.obeys_dst))

    print("\nIANA Timezone Fields:")
    print("  IANA Time Zone:  {}".format(metadata.iana_time_zone))
    print("  IANA UTC Offset: {}".format(metadata.iana_utc_offset))
    print("  IANA Obeys DST:  {}".format(metadata.iana_obeys_dst))

if __name__ == "__main__":
    run()
