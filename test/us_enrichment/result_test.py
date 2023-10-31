import unittest

from smartystreets_python_sdk.us_enrichment.response import Response

name_changes = {"1st_floor_sqft": "first_floor_sqft", "2nd_floor_sqft": "second_floor_sqft"}

class ResultTest(unittest.TestCase):
    def test_result_generic_deserialization(self):
        test_obj = {"smarty_key":"179317873","data_set_name":"property","data_subset_name":"principal",
                    "attributes":{"1st_floor_sqft":"1169","2nd_floor_sqft":"400","acres":"18.0000000",
                                  "assessed_improvement_percent":"0.00","assessed_improvement_value":"0",
                                  "assessed_land_value":"0","assessed_value":"125236","assessor_last_update":"2022-12-14",
                                  "assessor_taxroll_update":"2022-09-30","attic_area":"400","basement_sqft":"0",
                                  "bathrooms_partial":"1","bathrooms_total":"2.000","bedrooms":"1","building_definition_code":"living_area",
                                  "building_sqft":"2034","cbsa_code":"38900","cbsa_name":"Portland-Vancouver-Beaverton, OR-WA Metropolitan Statistical Area",
                                  "census_block":"1038","census_block_group":"1","census_tract":"24100","code_title_company":"0","combined_statistical_area":"Portland-Vancouver-Salem, OR-WA",
                                  "congressional_district":"331","contact_city":"Colton","contact_crrt":"R002","contact_full_address":"19768 S Harper Rd",
                                  "contact_house_number":"19768","contact_mail_info_format":"standard_us","contact_mailing_county":"Clackamas","contact_mailing_fips":"41005",
                                  "contact_pre_direction":"S","contact_state":"OR","contact_street_name":"Harper","contact_suffix":"Rd","contact_zip":"97017",
                                  "contact_zip4":"9417","deck_area":"0","deed_owner_first_name":"Lonny","deed_owner_full_name":"Lonny S Johnson","deed_owner_last_name":"Johnson",
                                  "deed_owner_middle_name":"S","deed_sale_price":"0","depth_linear_footage":"0.0","driveway_sqft":"0","elevation_feet":"708","exterior_walls":"other",
                                  "fence_area":"0","fips_code":"41005","fireplace":"yes","fireplace_number":"1","first_name":"Lonny","foundation":"block_unspecified",
                                  "garage_sqft":"0","gross_sqft":"2034","heat":"forced_air","instrument_date":"2018-06-01","land_use_code":"12","land_use_group":"residential",
                                  "land_use_standard":"rural_residence","last_name":"Johnson","latitude":"45.162895","legal_description":"Section 05 Township 5s Range 3e Tax Lot 02900",
                                  "loading_platform":"0","longitude":"-122.459463","lot_1":"2900","lot_sqft":"784080.00","market_improvement_percent":"19.00","market_improvement_value":"152680",
                                  "market_land_value":"618692","market_value_year":"2022","match_type":"parcel","middle_name":"S","minor_civil_division_code":"90595","minor_civil_division_name":"Colton",
                                  "msa_code":"38900","msa_name":"Portland-Vancouver-Beaverton, OR-WA","multi_parcel_flag":"0","neighborhood_code":"14","owner_full_name":"Lonny S Johnson",
                                  "owner_occupancy_status":"owner_occupied","ownership_type":"Individual","parcel_account_number":"01116946","parcel_number_year_added":"1993",
                                  "parcel_number_year_change":"0","parcel_raw_number":"53e05 02900","parking_spaces":"0","patio_area":"0","plumbing_fixtures_count":"0","pool_area":"0",
                                  "porch_area":"0","previous_assessed_value":"121694","property_address_carrier_route_code":"R002","property_address_city":"Colton","property_address_full":"19768 S Harper Rd",
                                  "property_address_house_number":"19768","property_address_pre_direction":"S","property_address_state":"OR","property_address_street_name":"Harper",
                                  "property_address_street_suffix":"Rd","property_address_zip_4":"9417","property_address_zipcode":"97017","publication_date":"2023-08-05",
                                  "range":"3e","recording_date":"2018-06-04","roof_cover":"composition_shingle","rooms":"0","sale_amount":"0","section":"05","situs_county":"Clackamas",
                                  "situs_state":"OR","stories_number":"1","tax_assess_year":"2022","tax_billed_amount":"1580.29","tax_fiscal_year":"2022","tax_jurisdiction":"Clackamas",
                                  "tax_rate_area":"053-007","total_market_value":"771372","township":"5s","tract_number":"0","transfer_amount":"0","unit_count":"0","upper_floors_sqft":"0",
                                  "width_linear_footage":"0.0","year_built":"1935","zoning":"Agf"
                                  }
                        }

        res = Response(test_obj)
        for key in test_obj.keys():
            if key == "attributes":
                attributes_obj = test_obj[key]
                for atr_key in attributes_obj.keys():
                    other_key = atr_key
                    if atr_key in name_changes.keys():
                        other_key = name_changes[atr_key]
                    self.assertEqual(attributes_obj[atr_key], res.attributes.__dict__[other_key])
            else:
                self.assertEqual(test_obj[key], eval(f"res.{key}"))
