from typing import Any, cast


class Response:
    def __init__(self, obj: dict) -> None:
        self.smarty_key: str | None = obj.get('smarty_key', None)
        self.matched_address: list[MatchedAddress] | None = get_matched_address(obj.get('matched_address', None))
        data_set_name: str | None = None
        data_subset_name: str | None = None
        if 'data_set_name' in obj:
            self.data_set_name: str | None = obj.get('data_set_name')
            data_set_name = obj.get('data_set_name')
        elif 'secondaries' in obj:
            data_set_name = 'secondary'

        if 'data_subset_name' in obj:
            self.data_subset_name: str | None = obj.get('data_subset_name', None)
            data_subset_name = obj.get('data_subset_name', None)
        elif 'count' in obj:
            data_set_name = 'secondary'
            data_subset_name = 'count'
            
        if data_set_name == 'secondary':
            if data_subset_name == 'count':
                self.count: int | None = obj.get('count', None)
            else:
                self.root_address: list[SecondaryRootAddress] | None = get_secondary_root_address(obj.get('root_address', None))
                if 'aliases' in obj:
                    self.aliases: list[SecondaryAliases] | None = get_secondary_aliases(obj.get('aliases', None))
                self.secondaries: list[SecondarySecondaries] | None = get_secondary_secondaries(obj.get('secondaries', None))
        else:
            self.attributes: PrincipalAttributes | GeoReferenceOutputCategories | None = get_attributes(data_set_name, data_subset_name, obj.get('attributes', None))

    def __str__(self) -> str:
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += get_lines(key, val)
        return '\n    '.join(lines)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, type(self)) and __value.smarty_key == self.smarty_key

def get_lines(key: str | int, val: Any) -> list[str]:
    lines = ['']
    if type(val) is list:
        if len(val) > 1:
            for item in val:
                if val.index(item) == 0:
                    lines += ['secondaries:']
                lines += get_lines(val.index(item), val[val.index(item)])
            return lines
        else:
            return get_lines(key, val[0])
    else:
        if type(key) == int:
            return '    {}: {}'.format(key, val).split('\n')
        return '{}: {}'.format(key, val).split('\n')

class MatchedAddress:
    def __init__(self, obj: dict) -> None:
        self.street: str | None = obj.get('street', None)
        self.city: str | None = obj.get('city', None)
        self.state: str | None = obj.get('state', None)
        self.zipcode: str | None = obj.get('zipcode', None)

    def __str__(self) -> str:
        lines = ['']
        for key, val in vars(self).items():
            if type(val) is list:
                lines.append(key + ': ')
                for item in val:
                    for subkey, subval in vars(item).items():
                        lines += '    {}: {}'.format(subkey, subval).split('\n')
            else:
                lines.append(key + ': ' + str(val))
        return '\n    '.join(lines)

def get_matched_address(matched_address_obj: dict | None) -> list[MatchedAddress] | None:
    if matched_address_obj is None:
        return None
    output: list[MatchedAddress] = []
    output.append(MatchedAddress(matched_address_obj))

    return output

def get_attributes(dataset: str | None, data_subset: str | None,
                   attribute_obj: dict | None) -> 'PrincipalAttributes | GeoReferenceOutputCategories | None':
    if dataset == "property":
        if data_subset == "principal":
            return PrincipalAttributes(cast(dict, attribute_obj))
    if dataset == "geo-reference":
        return GeoReferenceOutputCategories(cast(dict, attribute_obj))
    return None

class PrincipalAttributes:
    def __init__(self, obj: dict) -> None:
        self.first_floor_sqft: str | None = obj.get('1st_floor_sqft', None)
        self.second_floor_sqft: str | None = obj.get('2nd_floor_sqft', None)
        self.acres: str | None = obj.get('acres', None)
        self.air_conditioner: str | None = obj.get('air_conditioner', None)
        self.arbor_pergola: str | None = obj.get('arbor_pergola', None)
        self.assessed_improvement_percent: str | None = obj.get('assessed_improvement_percent', None)
        self.assessed_improvement_value: str | None = obj.get('assessed_improvement_value', None)
        self.assessed_land_value: str | None = obj.get('assessed_land_value', None)
        self.assessed_value: str | None = obj.get('assessed_value', None)
        self.assessor_last_update: str | None = obj.get('assessor_last_update', None)
        self.assessor_taxroll_update: str | None = obj.get('assessor_taxroll_update', None)
        self.attic_area: str | None = obj.get('attic_area', None)
        self.attic_flag: str | None = obj.get('attic_flag', None)
        self.balcony: str | None = obj.get('balcony', None)
        self.balcony_area: str | None = obj.get('balcony_area', None)
        self.basement_sqft: str | None = obj.get('basement_sqft', None)
        self.basement_sqft_finished: str | None = obj.get('basement_sqft_finished', None)
        self.basement_sqft_unfinished: str | None = obj.get('basement_sqft_unfinished', None)
        self.bath_house: str | None = obj.get('bath_house', None)
        self.bath_house_sqft: str | None = obj.get('bath_house_sqft', None)
        self.bathrooms_partial: str | None = obj.get('bathrooms_partial', None)
        self.bathrooms_total: str | None = obj.get('bathrooms_total', None)
        self.bedrooms: str | None = obj.get('bedrooms', None)
        self.block1: str | None = obj.get('block1', None)
        self.block2: str | None = obj.get('block2', None)
        self.boat_access: str | None = obj.get('boat_access', None)
        self.boat_house: str | None = obj.get('boat_house', None)
        self.boat_house_sqft: str | None = obj.get('boat_house_sqft', None)
        self.boat_lift: str | None = obj.get('boat_lift', None)
        self.bonus_room: str | None = obj.get('bonus_room', None)
        self.breakfast_nook: str | None = obj.get('breakfast_nook', None)
        self.breezeway: str | None = obj.get('breezeway', None)
        self.building_definition_code: str | None = obj.get('building_definition_code', None)
        self.building_sqft: str | None = obj.get('building_sqft', None)
        self.cabin: str | None = obj.get('cabin', None)
        self.cabin_sqft: str | None = obj.get('cabin_sqft', None)
        self.canopy: str | None = obj.get('canopy', None)
        self.canopy_sqft: str | None = obj.get('canopy_sqft', None)
        self.carport: str | None = obj.get('carport', None)
        self.carport_sqft: str | None = obj.get('carport_sqft', None)
        self.cbsa_code: str | None = obj.get('cbsa_code', None)
        self.cbsa_name: str | None = obj.get('cbsa_name', None)
        self.cellar: str | None = obj.get('cellar', None)
        self.census_block: str | None = obj.get('census_block', None)
        self.census_block_group: str | None = obj.get('census_block_group', None)
        self.census_fips_place_code: str | None = obj.get('census_fips_place_code', None)
        self.census_tract: str | None = obj.get('census_tract', None)
        self.central_vacuum: str | None = obj.get('central_vacuum', None)
        self.code_title_company: str | None = obj.get('code_title_company', None)
        self.combined_statistical_area: str | None = obj.get('combined_statistical_area', None)
        self.community_rec: str | None = obj.get('community_rec', None)
        self.company_flag: str | None = obj.get('company_flag', None)
        self.congressional_district: str | None = obj.get('congressional_district', None)
        self.contact_city: str | None = obj.get('contact_city', None)
        self.contact_crrt: str | None = obj.get('contact_crrt', None)
        self.contact_full_address: str | None = obj.get('contact_full_address', None)
        self.contact_house_number: str | None = obj.get('contact_house_number', None)
        self.contact_mail_info_format: str | None = obj.get('contact_mail_info_format', None)
        self.contact_mail_info_privacy: str | None = obj.get('contact_mail_info_privacy', None)
        self.contact_mailing_county: str | None = obj.get('contact_mailing_county', None)
        self.contact_mailing_fips: str | None = obj.get('contact_mailing_fips', None)
        self.contact_post_direction: str | None = obj.get('contact_post_direction', None)
        self.contact_pre_direction: str | None = obj.get('contact_pre_direction', None)
        self.contact_state: str | None = obj.get('contact_state', None)
        self.contact_street_name: str | None = obj.get('contact_street_name', None)
        self.contact_suffix: str | None = obj.get('contact_suffix', None)
        self.contact_unit_designator: str | None = obj.get('contact_unit_designator', None)
        self.contact_value: str | None = obj.get('contact_value', None)
        self.contact_zip: str | None = obj.get('contact_zip', None)
        self.contact_zip4: str | None = obj.get('contact_zip4', None)
        self.courtyard: str | None = obj.get('courtyard', None)
        self.courtyard_area: str | None = obj.get('courtyard_area', None)
        self.deck: str | None = obj.get('deck', None)
        self.deck_area: str | None = obj.get('deck_area', None)
        self.deed_document_page: str | None = obj.get('deed_document_page', None)
        self.deed_document_book: str | None = obj.get('deed_document_book', None)
        self.deed_document_number: str | None = obj.get('deed_document_number', None)
        self.deed_owner_first_name: str | None = obj.get('deed_owner_first_name', None)
        self.deed_owner_first_name2: str | None = obj.get('deed_owner_first_name2', None)
        self.deed_owner_first_name3: str | None = obj.get('deed_owner_first_name3', None)
        self.deed_owner_first_name4: str | None = obj.get('deed_owner_first_name4', None)
        self.deed_owner_full_name: str | None = obj.get('deed_owner_full_name', None)
        self.deed_owner_full_name2: str | None = obj.get('deed_owner_full_name2', None)
        self.deed_owner_full_name3: str | None = obj.get('deed_owner_full_name3', None)
        self.deed_owner_full_name4: str | None = obj.get('deed_owner_full_name4', None)
        self.deed_owner_last_name: str | None = obj.get('deed_owner_last_name', None)
        self.deed_owner_last_name2: str | None = obj.get('deed_owner_last_name2', None)
        self.deed_owner_last_name3: str | None = obj.get('deed_owner_last_name3', None)
        self.deed_owner_last_name4: str | None = obj.get('deed_owner_last_name4', None)
        self.deed_owner_middle_name: str | None = obj.get('deed_owner_middle_name', None)
        self.deed_owner_middle_name = obj.get('deed_owner_middle_name', None)
        self.deed_owner_middle_name2: str | None = obj.get('deed_owner_middle_name2', None)
        self.deed_owner_middle_name3: str | None = obj.get('deed_owner_middle_name3', None)
        self.deed_owner_middle_name4: str | None = obj.get('deed_owner_middle_name4', None)
        self.deed_owner_suffix: str | None = obj.get('deed_owner_suffix', None)
        self.deed_owner_suffix2: str | None = obj.get('deed_owner_suffix2', None)
        self.deed_owner_suffix3: str | None = obj.get('deed_owner_suffix3', None)
        self.deed_owner_suffix4: str | None = obj.get('deed_owner_suffix4', None)
        self.deed_sale_date: str | None = obj.get('deed_sale_date', None)
        self.deed_sale_price: str | None = obj.get('deed_sale_price', None)
        self.deed_transaction_id: str | None = obj.get('deed_transaction_id', None)
        self.depth_linear_footage: str | None = obj.get('depth_linear_footage', None)
        self.disabled_tax_exemption: str | None = obj.get('disabled_tax_exemption', None)
        self.document_type_description: str | None = obj.get('document_type_description', None)
        self.driveway_sqft: str | None = obj.get('driveway_sqft', None)
        self.driveway_type: str | None = obj.get('driveway_type', None)
        self.effective_year_built: str | None = obj.get('effective_year_built', None)
        self.elevation_feet: str | None = obj.get('elevation_feet', None)
        self.elevator: str | None = obj.get('elevator', None)
        self.equestrian_arena: str | None = obj.get('equestrian_arena', None)
        self.escalator: str | None = obj.get('escalator', None)
        self.exercise_room: str | None = obj.get('exercise_room', None)
        self.exterior_walls: str | None = obj.get('exterior_walls', None)
        self.family_room: str | None = obj.get('family_room', None)
        self.fence: str | None = obj.get('fence', None)
        self.fence_area: str | None = obj.get('fence_area', None)
        self.financial_history: list[FinancialHistory] | None = get_financial_history(obj.get('financial_history', None))
        self.fips_code: str | None = obj.get('fips_code', None)
        self.fire_resistance_code: str | None = obj.get('fire_resistance_code', None)
        self.fire_sprinklers_flag: str | None = obj.get('fire_sprinklers_flag', None)
        self.fireplace: str | None = obj.get('fireplace', None)
        self.fireplace_number: str | None = obj.get('fireplace_number', None)
        self.first_name: str | None = obj.get('first_name', None)
        self.first_name_2: str | None = obj.get('first_name_2', None)
        self.first_name_3: str | None = obj.get('first_name_3', None)
        self.first_name_4: str | None = obj.get('first_name_4', None)
        self.flooring: str | None = obj.get('flooring', None)
        self.foundation: str | None = obj.get('foundation', None)
        self.game_room: str | None = obj.get('game_room', None)
        self.garage: str | None = obj.get('garage', None)
        self.garage_sqft: str | None = obj.get('garage_sqft', None)
        self.gazebo: str | None = obj.get('gazebo', None)
        self.gazebo_sqft: str | None = obj.get('gazebo_sqft', None)
        self.golf_course: str | None = obj.get('golf_course', None)
        self.grainery: str | None = obj.get('grainery', None)
        self.grainery_sqft: str | None = obj.get('grainery_sqft', None)
        self.great_room: str | None = obj.get('great_room', None)
        self.greenhouse: str | None = obj.get('greenhouse', None)
        self.greenhouse_sqft: str | None = obj.get('greenhouse_sqft', None)
        self.gross_sqft: str | None = obj.get('gross_sqft', None)
        self.guesthouse: str | None = obj.get('guesthouse', None)
        self.guesthouse_sqft: str | None = obj.get('guesthouse_sqft', None)
        self.handicap_accessibility: str | None = obj.get('handicap_accessibility', None)
        self.heat: str | None = obj.get('heat', None)
        self.heat_fuel_type: str | None = obj.get('heat_fuel_type', None)
        self.hobby_room: str | None = obj.get('hobby_room', None)
        self.homeowner_tax_exemption: str | None = obj.get('homeowner_tax_exemption', None)
        self.instrument_date: str | None = obj.get('instrument_date', None)
        self.intercom_system: str | None = obj.get('intercom_system', None)
        self.interest_rate_type_2: str | None = obj.get('interest_rate_type_2', None)
        self.interior_structure: str | None = obj.get('interior_structure', None)
        self.kennel: str | None = obj.get('kennel', None)
        self.kennel_sqft: str | None = obj.get('kennel_sqft', None)
        self.land_use_code: str | None = obj.get('land_use_code', None)
        self.land_use_group: str | None = obj.get('land_use_group', None)
        self.land_use_standard: str | None = obj.get('land_use_standard', None)
        self.last_name: str | None = obj.get('last_name', None)
        self.last_name_2: str | None = obj.get('last_name_2', None)
        self.last_name_3: str | None = obj.get('last_name_3', None)
        self.last_name_4: str | None = obj.get('last_name_4', None)
        self.latitude: str | None = obj.get('latitude', None)
        self.laundry: str | None = obj.get('laundry', None)
        self.lean_to: str | None = obj.get('lean_to', None)
        self.lean_to_sqft: str | None = obj.get('lean_to_sqft', None)
        self.legal_description: str | None = obj.get('legal_description', None)
        self.legal_unit: str | None = obj.get('legal_unit', None)
        self.lender_address: str | None = obj.get('lender_address', None)
        self.lender_address_2: str | None = obj.get('lender_address_2', None)
        self.lender_city: str | None = obj.get('lender_city', None)
        self.lender_city_2: str | None = obj.get('lender_city_2', None)
        self.lender_code_2: str | None = obj.get('lender_code_2', None)
        self.lender_first_name: str | None = obj.get('lender_first_name', None)
        self.lender_first_name_2: str | None = obj.get('lender_first_name_2', None)
        self.lender_last_name: str | None = obj.get('lender_last_name', None)
        self.lender_last_name_2: str | None = obj.get('lender_last_name_2', None)
        self.lender_name: str | None = obj.get('lender_name', None)
        self.lender_name_2: str | None = obj.get('lender_name_2', None)
        self.lender_seller_carry_back: str | None = obj.get('lender_seller_carry_back', None)
        self.lender_seller_carry_back_2: str | None = obj.get('lender_seller_carry_back_2', None)
        self.lender_state: str | None = obj.get('lender_state', None)
        self.lender_state_2: str | None = obj.get('lender_state_2', None)
        self.lender_zip: str | None = obj.get('lender_zip', None)
        self.lender_zip_2: str | None = obj.get('lender_zip_2', None)
        self.lender_zip_extended: str | None = obj.get('lender_zip_extended', None)
        self.lender_zip_extended_2: str | None = obj.get('lender_zip_extended_2', None)
        self.loading_platform: str | None = obj.get('loading_platform', None)
        self.loading_platform_sqft: str | None = obj.get('loading_platform_sqft', None)
        self.longitude: str | None = obj.get('longitude', None)
        self.lot_1: str | None = obj.get('lot_1', None)
        self.lot_2: str | None = obj.get('lot_2', None)
        self.lot_3: str | None = obj.get('lot_3', None)
        self.lot_sqft: str | None = obj.get('lot_sqft', None)
        self.market_improvement_percent: str | None = obj.get('market_improvement_percent', None)
        self.market_improvement_value: str | None = obj.get('market_improvement_value', None)
        self.market_land_value: str | None = obj.get('market_land_value', None)
        self.market_value_year: str | None = obj.get('market_value_year', None)
        self.match_type: str | None = obj.get('match_type', None)
        self.media_room: str | None = obj.get('media_room', None)
        self.metro_division: str | None = obj.get('metro_division', None)
        self.middle_name: str | None = obj.get('middle_name', None)
        self.middle_name_2: str | None = obj.get('middle_name_2', None)
        self.middle_name_3: str | None = obj.get('middle_name_3', None)
        self.middle_name_4: str | None = obj.get('middle_name_4', None)
        self.milkhouse: str | None = obj.get('milkhouse', None)
        self.milkhouse_sqft: str | None = obj.get('milkhouse_sqft', None)
        self.minor_civil_division_code: str | None = obj.get('minor_civil_division_code', None)
        self.minor_civil_division_name: str | None = obj.get('minor_civil_division_name', None)
        self.mobile_home_hookup: str | None = obj.get('mobile_home_hookup', None)
        self.mortgage_amount: str | None = obj.get('mortgage_amount', None)
        self.mortgage_amount_2: str | None = obj.get('mortgage_amount_2', None)
        self.mortgage_due_date: str | None = obj.get('mortgage_due_date', None)
        self.mortgage_due_date_2: str | None = obj.get('mortgage_due_date_2', None)
        self.mortgage_interest_rate: str | None = obj.get('mortgage_interest_rate', None)
        self.mortgage_interest_rate_type: str | None = obj.get('mortgage_interest_rate_type', None)
        self.mortgage_lender_code: str | None = obj.get('mortgage_lender_code', None)
        self.mortgage_rate_2: str | None = obj.get('mortgage_rate_2', None)
        self.mortgage_recording_date: str | None = obj.get('mortgage_recording_date', None)
        self.mortgage_recording_date_2: str | None = obj.get('mortgage_recording_date_2', None)
        self.mortgage_term: str | None = obj.get('mortgage_term', None)
        self.mortgage_term_2: str | None = obj.get('mortgage_term_2', None)
        self.mortgage_term_type: str | None = obj.get('mortgage_term_type', None)
        self.mortgage_term_type_2: str | None = obj.get('mortgage_term_type_2', None)
        self.mortgage_type: str | None = obj.get('mortgage_type', None)
        self.mortgage_type_2: str | None = obj.get('mortgage_type_2', None)
        self.msa_code: str | None = obj.get('msa_code', None)
        self.msa_name: str | None = obj.get('msa_name', None)
        self.mud_room: str | None = obj.get('mud_room', None)
        self.multi_parcel_flag: str | None = obj.get('multi_parcel_flag', None)
        self.name_title_company: str | None = obj.get('name_title_company', None)
        self.neighborhood_code: str | None = obj.get('neighborhood_code', None)
        self.number_of_buildings: str | None = obj.get('number_of_buildings', None)
        self.office: str | None = obj.get('office', None)
        self.office_sqft: str | None = obj.get('office_sqft', None)
        self.other_tax_exemption: str | None = obj.get('other_tax_exemption', None)
        self.outdoor_kitchen_fireplace: str | None = obj.get('outdoor_kitchen_fireplace', None)
        self.overhead_door: str | None = obj.get('overhead_door', None)
        self.owner_full_name: str | None = obj.get('owner_full_name', None)
        self.owner_full_name_2: str | None = obj.get('owner_full_name_2', None)
        self.owner_full_name_3: str | None = obj.get('owner_full_name_3', None)
        self.owner_full_name_4: str | None = obj.get('owner_full_name_4', None)
        self.owner_occupancy_status: str | None = obj.get('owner_occupancy_status', None)
        self.ownership_transfer_date: str | None = obj.get('ownership_transfer_date', None)
        self.ownership_transfer_doc_number: str | None = obj.get('ownership_transfer_doc_number', None)
        self.ownership_transfer_transaction_id: str | None = obj.get('ownership_transfer_transaction_id', None)
        self.ownership_type: str | None = obj.get('ownership_type', None)
        self.ownership_type_2: str | None = obj.get('ownership_type_2', None)
        self.ownership_vesting_relation_code: str | None = obj.get('ownership_vesting_relation_code', None)
        self.parcel_account_number: str | None = obj.get('parcel_account_number', None)
        self.parcel_map_book: str | None = obj.get('parcel_map_book', None)
        self.parcel_map_page: str | None = obj.get('parcel_map_page', None)
        self.parcel_number_alternate: str | None = obj.get('parcel_number_alternate', None)
        self.parcel_number_formatted: str | None = obj.get('parcel_number_formatted', None)
        self.parcel_number_previous: str | None = obj.get('parcel_number_previous', None)
        self.parcel_number_year_added: str | None = obj.get('parcel_number_year_added', None)
        self.parcel_number_year_change: str | None = obj.get('parcel_number_year_change', None)
        self.parcel_raw_number: str | None = obj.get('parcel_raw_number', None)
        self.parcel_shell_record: str | None = obj.get('parcel_shell_record', None)
        self.parking_spaces: str | None = obj.get('parking_spaces', None)
        self.patio_area: str | None = obj.get('patio_area', None)
        self.phase_name: str | None = obj.get('phase_name', None)
        self.plumbing_fixtures_count: str | None = obj.get('plumbing_fixtures_count', None)
        self.pole_struct: str | None = obj.get('pole_struct', None)
        self.pole_struct_sqft: str | None = obj.get('pole_struct_sqft', None)
        self.pond: str | None = obj.get('pond', None)
        self.pool: str | None = obj.get('pool', None)
        self.pool_area: str | None = obj.get('pool_area', None)
        self.poolhouse: str | None = obj.get('poolhouse', None)
        self.poolhouse_sqft: str | None = obj.get('poolhouse_sqft', None)
        self.porch: str | None = obj.get('porch', None)
        self.porch_area: str | None = obj.get('porch_area', None)
        self.poultry_house: str | None = obj.get('poultry_house', None)
        self.poultry_house_sqft: str | None = obj.get('poultry_house_sqft', None)
        self.previous_assessed_value: str | None = obj.get('previous_assessed_value', None)
        self.prior_sale_amount: str | None = obj.get('prior_sale_amount', None)
        self.prior_sale_date: str | None = obj.get('prior_sale_date', None)
        self.property_address_carrier_route_code: str | None = obj.get('property_address_carrier_route_code', None)
        self.property_address_city: str | None = obj.get('property_address_city', None)
        self.property_address_full: str | None = obj.get('property_address_full', None)
        self.property_address_house_number: str | None = obj.get('property_address_house_number', None)
        self.property_address_post_direction: str | None = obj.get('property_address_post_direction', None)
        self.property_address_pre_direction: str | None = obj.get('property_address_pre_direction', None)
        self.property_address_state: str | None = obj.get('property_address_state', None)
        self.property_address_street_name: str | None = obj.get('property_address_street_name', None)
        self.property_address_street_suffix: str | None = obj.get('property_address_street_suffix', None)
        self.property_address_unit_designator: str | None = obj.get('property_address_unit_designator', None)
        self.property_address_unit_value: str | None = obj.get('property_address_unit_value', None)
        self.property_address_zip_4: str | None = obj.get('property_address_zip_4', None)
        self.property_address_zipcode: str | None = obj.get('property_address_zipcode', None)
        self.publication_date: str | None = obj.get('publication_date', None)
        self.quarter: str | None = obj.get('quarter', None)
        self.quarter_quarter: str | None = obj.get('quarter_quarter', None)
        self.quonset: str | None = obj.get('quonset', None)
        self.quonset_sqft: str | None = obj.get('quonset_sqft', None)
        self.range: str | None = obj.get('range', None)
        self.recording_date: str | None = obj.get('recording_date', None)
        self.roof_cover: str | None = obj.get('roof_cover', None)
        self.roof_frame: str | None = obj.get('roof_frame', None)
        self.rooms: str | None = obj.get('rooms', None)
        self.rv_parking: str | None = obj.get('rv_parking', None)
        self.safe_room: str | None = obj.get('safe_room', None)
        self.sale_amount: str | None = obj.get('sale_amount', None)
        self.sale_date: str | None = obj.get('sale_date', None)
        self.sauna: str | None = obj.get('sauna', None)
        self.section: str | None = obj.get('section', None)
        self.security_alarm: str | None = obj.get('security_alarm', None)
        self.senior_tax_exemption: str | None = obj.get('senior_tax_exemption', None)
        self.sewer_type: str | None = obj.get('sewer_type', None)
        self.shed: str | None = obj.get('shed', None)
        self.shed_sqft: str | None = obj.get('shed_sqft', None)
        self.silo: str | None = obj.get('silo', None)
        self.silo_sqft: str | None = obj.get('silo_sqft', None)
        self.sitting_room: str | None = obj.get('sitting_room', None)
        self.situs_county: str | None = obj.get('situs_county', None)
        self.situs_state: str | None = obj.get('situs_state', None)
        self.sound_system: str | None = obj.get('sound_system', None)
        self.sports_court: str | None = obj.get('sports_court', None)
        self.sprinklers: str | None = obj.get('sprinklers', None)
        self.stable: str | None = obj.get('stable', None)
        self.stable_sqft: str | None = obj.get('stable_sqft', None)
        self.storage_building: str | None = obj.get('storage_building', None)
        self.storage_building_sqft: str | None = obj.get('storage_building_sqft', None)
        self.stories_number: str | None = obj.get('stories_number', None)
        self.storm_shelter: str | None = obj.get('storm_shelter', None)
        self.storm_shutter: str | None = obj.get('storm_shutter', None)
        self.structure_style: str | None = obj.get('structure_style', None)
        self.study: str | None = obj.get('study', None)
        self.subdivision: str | None = obj.get('subdivision', None)
        self.suffix: str | None = obj.get('suffix', None)
        self.suffix_2: str | None = obj.get('suffix_2', None)
        self.suffix_3: str | None = obj.get('suffix_3', None)
        self.suffix_4: str | None = obj.get('suffix_4', None)
        self.sunroom: str | None = obj.get('sunroom', None)
        self.tax_assess_year: str | None = obj.get('tax_assess_year', None)
        self.tax_billed_amount: str | None = obj.get('tax_billed_amount', None)
        self.tax_delinquent_year: str | None = obj.get('tax_delinquent_year', None)
        self.tax_fiscal_year: str | None = obj.get('tax_fiscal_year', None)
        self.tax_jurisdiction: str | None = obj.get('tax_jurisdiction', None)
        self.tax_rate_area: str | None = obj.get('tax_rate_area', None)
        self.tennis_court: str | None = obj.get('tennis_court', None)
        self.topography_code: str | None = obj.get('topography_code', None)
        self.total_market_value: str | None = obj.get('total_market_value', None)
        self.township: str | None = obj.get('township', None)
        self.tract_number: str | None = obj.get('tract_number', None)
        self.transfer_amount: str | None = obj.get('transfer_amount', None)
        self.trust_description: str | None = obj.get('trust_description', None)
        self.unit_count: str | None = obj.get('unit_count', None)
        self.upper_floors_sqft: str | None = obj.get('upper_floors_sqft', None)
        self.utility: str | None = obj.get('utility', None)
        self.utility_building: str | None = obj.get('utility_building', None)
        self.utility_building_sqft: str | None = obj.get('utility_building_sqft', None)
        self.utility_sqft: str | None = obj.get('utility_sqft', None)
        self.veteran_tax_exemption: str | None = obj.get('veteran_tax_exemption', None)
        self.view_description: str | None = obj.get('view_description', None)
        self.water_feature: str | None = obj.get('water_feature', None)
        self.water_service_type: str | None = obj.get('water_service_type', None)
        self.wet_bar: str | None = obj.get('wet_bar', None)
        self.widow_tax_exemption: str | None = obj.get('widow_tax_exemption', None)
        self.width_linear_footage: str | None = obj.get('width_linear_footage', None)
        self.wine_cellar: str | None = obj.get('wine_cellar', None)
        self.year_built: str | None = obj.get('year_built', None)
        self.zoning: str | None = obj.get('zoning', None)

    def __str__(self) -> str:
        lines = ['']
        for key, val in vars(self).items():
            if type(val) is list:
                lines.append(key + ': ')
                for item in val:
                    for subkey, subval in vars(item).items():
                        lines += '    {}: {}'.format(subkey, subval).split('\n')
            else:
                lines.append(key + ': ' + str(val))
        return '\n    '.join(lines)


def get_financial_history(financial_history_obj: list[dict] | None) -> 'list[FinancialHistory] | None':
    if financial_history_obj is None:
        return None
    output: list[FinancialHistory] = []
    for obj in financial_history_obj:
        output.append(FinancialHistory(obj))
    return output


class FinancialHistory:
    def __init__(self, obj: dict) -> None:
        self.code_title_company: str | None = obj.get('code_title_company', None)
        self.document_type_description: str | None = obj.get('document_type_description', None)
        self.instrument_date: str | None = obj.get('instrument_date', None)
        self.interest_rate_type_2: str | None = obj.get('interest_rate_type_2', None)
        self.lender_address: str | None = obj.get('lender_address', None)
        self.lender_address_2: str | None = obj.get('lender_address_2', None)
        self.lender_city: str | None = obj.get('lender_city', None)
        self.lender_city_2: str | None = obj.get('lender_city_2', None)
        self.lender_code_2: str | None = obj.get('lender_code_2', None)
        self.lender_first_name: str | None = obj.get('lender_first_name', None)
        self.lender_first_name_2: str | None = obj.get('lender_first_name_2', None)
        self.lender_last_name: str | None = obj.get('lender_last_name', None)
        self.lender_last_name_2: str | None = obj.get('lender_last_name_2', None)
        self.lender_name: str | None = obj.get('lender_name', None)
        self.lender_name_2: str | None = obj.get('lender_name_2', None)
        self.lender_seller_carry_back: str | None = obj.get('lender_seller_carry_back', None)
        self.lender_seller_carry_back_2: str | None = obj.get('lender_seller_carry_back_2', None)
        self.lender_state: str | None = obj.get('lender_state', None)
        self.lender_state_2: str | None = obj.get('lender_state_2', None)
        self.lender_zip: str | None = obj.get('lender_zip', None)
        self.lender_zip_2: str | None = obj.get('lender_zip_2', None)
        self.lender_zip_extended: str | None = obj.get('lender_zip_extended', None)
        self.lender_zip_extended_2: str | None = obj.get('lender_zip_extended_2', None)
        self.mortgage_amount: str | None = obj.get('mortgage_amount', None)
        self.mortgage_amount_2: str | None = obj.get('mortgage_amount_2', None)
        self.mortgage_due_date: str | None = obj.get('mortgage_due_date', None)
        self.mortgage_due_date_2: str | None = obj.get('mortgage_due_date_2', None)
        self.mortgage_interest_rate: str | None = obj.get('mortgage_interest_rate', None)
        self.mortgage_interest_rate_type: str | None = obj.get('mortgage_interest_rate_type', None)
        self.mortgage_lender_code: str | None = obj.get('mortgage_lender_code', None)
        self.mortgage_rate_2: str | None = obj.get('mortgage_rate_2', None)
        self.mortgage_recording_date: str | None = obj.get('mortgage_recording_date', None)
        self.mortgage_recording_date_2: str | None = obj.get('mortgage_recording_date_2', None)
        self.mortgage_term: str | None = obj.get('mortgage_term', None)
        self.mortgage_term_2: str | None = obj.get('mortgage_term_2', None)
        self.mortgage_term_type: str | None = obj.get('mortgage_term_type', None)
        self.mortgage_term_type_2: str | None = obj.get('mortgage_term_type_2', None)
        self.mortgage_type: str | None = obj.get('mortgage_type', None)
        self.mortgage_type_2: str | None = obj.get('mortgage_type_2', None)
        self.multi_parcel_flag: str | None = obj.get('multi_parcel_flag', None)
        self.name_title_company: str | None = obj.get('name_title_company', None)
        self.recording_date: str | None = obj.get('recording_date', None)
        self.transfer_amount: str | None = obj.get('transfer_amount', None)

    def __str__(self) -> str:
        return self.__dict__.__str__()

class GeoReferenceOutputCategories:
    def __init__(self, obj: dict) -> None:
        
        self.census_block: list[GeoReferenceCensusBlock] | None = get_geo_reference_census_block(obj.get('census_block', None))
        self.census_county_division: list[GeoReferenceCensusCountyDivision] | None = get_geo_reference_census_county_division(obj.get('census_county_division', None))
        self.census_tract: list[GeoReferenceCensusTract] | None = get_geo_reference_census_tract(obj.get('census_tract', None))
        self.core_based_stat_area: list[GeoReferenceCoreBasedStatArea] | None = get_geo_reference_core_based_stat_area(obj.get('core_based_stat_area', None))
        self.place: list[GeoReferencePlace] | None = get_geo_reference_place(obj.get('place', None))

    def __str__(self) -> str:
        lines = ['']
        for key, val in vars(self).items():
            if type(val) is list:
                lines.append(key + ': ')
                for item in val:
                    for subkey, subval in vars(item).items():
                        lines += '    {}: {}'.format(subkey, subval).split('\n')
            else:
                lines.append(key + ': ' + str(val))
        return '\n    '.join(lines)

class GeoReferenceCensusBlock:
    def __init__(self, obj: dict) -> None:
        self.accuracy: str | None = obj.get('accuracy', None)
        self.geoid: str | None = obj.get('geoid', None)

    def __str__(self) -> str:
        return self.__dict__.__str__()
    
def get_geo_reference_census_block(geo_reference_census_block_obj: dict | None) -> list[GeoReferenceCensusBlock] | None:
    if geo_reference_census_block_obj is None:
        return None
    output: list[GeoReferenceCensusBlock] = []
    output.append(GeoReferenceCensusBlock(geo_reference_census_block_obj))
    return output

class GeoReferenceCensusCountyDivision:
    def __init__(self, obj: dict) -> None:
        self.accuracy: str | None = obj.get('accuracy', None)
        self.code: str | None = obj.get('code', None)
        self.name: str | None = obj.get('name', None)

    def __str__(self) -> str:
        return self.__dict__.__str__()
    
def get_geo_reference_census_county_division(geo_reference_census_county_division_obj: dict | None) -> list[GeoReferenceCensusCountyDivision] | None:
    if geo_reference_census_county_division_obj is None:
        return None
    output: list[GeoReferenceCensusCountyDivision] = []
    output.append(GeoReferenceCensusCountyDivision(geo_reference_census_county_division_obj))
    return output

class GeoReferenceCensusTract:
    def __init__(self, obj: dict) -> None:
        self.code: str | None = obj.get('code', None)

    def __str__(self) -> str:
        return self.__dict__.__str__()
    
def get_geo_reference_census_tract(geo_reference_census_tract_obj: dict | None) -> list[GeoReferenceCensusTract] | None:
    if geo_reference_census_tract_obj is None:
        return None
    output: list[GeoReferenceCensusTract] = []
    output.append(GeoReferenceCensusTract(geo_reference_census_tract_obj))
    return output

class GeoReferenceCoreBasedStatArea:
    def __init__(self, obj: dict) -> None:
        self.code: str | None = obj.get('code', None)
        self.name: str | None = obj.get('name', None)

    def __str__(self) -> str:
        return self.__dict__.__str__()
    
def get_geo_reference_core_based_stat_area(geo_reference_core_based_stat_area_obj: dict | None) -> list[GeoReferenceCoreBasedStatArea] | None:
    if geo_reference_core_based_stat_area_obj is None:
        return None
    output: list[GeoReferenceCoreBasedStatArea] = []
    output.append(GeoReferenceCoreBasedStatArea(geo_reference_core_based_stat_area_obj))
    return output

class GeoReferencePlace:
    def __init__(self, obj: dict) -> None:
        self.accuracy: str | None = obj.get('accuracy', None)
        self.code: str | None = obj.get('code', None)
        self.name: str | None = obj.get('name', None)
        self.type: str | None = obj.get('type', None)

    def __str__(self) -> str:
        return self.__dict__.__str__()

def get_geo_reference_place(geo_reference_place_obj: dict | None) -> list[GeoReferencePlace] | None:
    if geo_reference_place_obj is None:
        return None
    output: list[GeoReferencePlace] = []
    output.append(GeoReferencePlace(geo_reference_place_obj))
    return output

class SecondaryRootAddress:
    def __init__(self, obj: dict) -> None:
        self.secondary_count: int | None = obj.get('secondary_count', None)
        self.smarty_key: str | None = obj.get('smarty_key', None)
        self.primary_number: str | None = obj.get('primary_number', None)
        self.street_predirection: str | None = obj.get('street_predirection', None)
        self.street_name: str | None = obj.get('street_name', None)
        self.street_suffix: str | None = obj.get('street_suffix', None)
        self.street_postdirection: str | None = obj.get('street_postdirection', None)
        self.city_name: str | None = obj.get('city_name', None)
        self.state_abbreviation: str | None = obj.get('state_abbreviation', None)
        self.zipcode: str | None = obj.get('zipcode', None)
        self.plus4_code: str | None = obj.get('plus4_code', None)

    def __str__(self) -> str:
        lines = ['']
        for key, val in vars(self).items():
            if type(val) is list:
                lines.append(key + ': ')
                for item in val:
                    for subkey, subval in vars(item).items():
                        lines += '    {}: {}'.format(subkey, subval).split('\n')
            else:
                lines.append(key + ': ' + str(val))
        return '\n    '.join(lines)

def get_secondary_root_address(secondary_root_address_obj: dict | None) -> list[SecondaryRootAddress] | None:
    if secondary_root_address_obj is None:
        return None
    output: list[SecondaryRootAddress] = []
    output.append(SecondaryRootAddress(secondary_root_address_obj))

    return output

class SecondaryAliases:
    def __init__(self, obj: dict) -> None:
        self.smarty_key: str | None = obj.get('smarty_key', None)
        self.primary_number: str | None = obj.get('primary_number', None)
        self.street_predirection: str | None = obj.get('street_predirection', None)
        self.street_name: str | None = obj.get('street_name', None)
        self.street_suffix: str | None = obj.get('street_suffix', None)
        self.street_postdirection: str | None = obj.get('street_postdirection', None)
        self.city_name: str | None = obj.get('city_name', None)
        self.state_abbreviation: str | None = obj.get('state_abbreviation', None)
        self.zipcode: str | None = obj.get('zipcode', None)
        self.plus4_code: str | None = obj.get('plus4_code', None)

    def __str__(self) -> str:
        lines = ['']
        for key, val in vars(self).items():
            if type(val) is list:
                lines.append(key + ': ')
                for item in val:
                    for subkey, subval in vars(item).items():
                        lines += '    {}: {}'.format(subkey, subval).split('\n')
            else:
                lines.append(key + ': ' + str(val))
        return '\n    '.join(lines)

def get_secondary_aliases(secondary_aliases_obj: list[dict] | None) -> list[SecondaryAliases] | None:
    if secondary_aliases_obj is None:
        return None
    output: list[SecondaryAliases] = []
    for item in secondary_aliases_obj:
        output.append(SecondaryAliases(item))
    return output

class SecondarySecondaries:
    def __init__(self, obj: dict) -> None:
        self.smarty_key: str | None = obj.get('smarty_key', None)
        self.secondary_designator: str | None = obj.get('secondary_designator', None)
        self.secondary_number: str | None = obj.get('secondary_number', None)
        self.plus4_code: str | None = obj.get('plus4_code', None)

    def __str__(self) -> str:
        lines = ['']
        for key, val in vars(self).items():
            if type(val) is list:
                lines.append(key + ': ')
                for item in val:
                    for subkey, subval in vars(item).items():
                        lines += '    {}: {}'.format(subkey, subval).split('\n')
            else:
                lines.append(key + ': ' + str(val))
        return '\n    '.join(lines)

def get_secondary_secondaries(secondary_secondaries_obj: list[dict] | None) -> list[SecondarySecondaries] | None:
    if secondary_secondaries_obj is None:
        return None
    output: list[SecondarySecondaries] = []
    for item in secondary_secondaries_obj:
        output.append(SecondarySecondaries(item))
    return output

class SecondaryCountAttributes:
    def __init__(self, obj: dict) -> None:
        self.smarty_key: str | None = obj.get('smarty_key', None)
        self.count: int | None = obj.get('count', None)

    def __str__(self) -> str:
        return self.__dict__.__str__()