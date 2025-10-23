# -*- coding: utf-8 -*-
import os
import json

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType


def run():
    # For client-side requests (browser/mobile), use this code:
    # key = os.environ['SMARTY_AUTH_WEB']
    # hostname = os.environ['SMARTY_WEBSITE_DOMAIN']
    # credentials = SharedCredentials(key, hostname)

    # For server-to-server requests, use this code:
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ( ClientBuilder(credentials)
        .with_feature_component_analysis() #  To add component analysis feature you need to specify when you create the client.
        .build_us_street_api_client()
    )

    lookup = StreetLookup()
    lookup.street = "1 Rosedale"
    lookup.secondary = "APT 2"
    lookup.city = "Baltimore"
    lookup.state = "MD"
    lookup.zipcode = "21229"
    lookup.match = MatchType.ENHANCED # Enhanced matching is required to return component analysis results.

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result

    if not result:
        return

    first_candidate = result[0]
    
    # Here is an example of how to access the result of component analysis.
    componentAnalysis = first_candidate.analysis.components
    print("Component Analysis Results:")
    print(json.dumps(componentAnalysis.__dict__, default=lambda o: o.__dict__, indent=2))

if __name__ == "__main__":
    run()
