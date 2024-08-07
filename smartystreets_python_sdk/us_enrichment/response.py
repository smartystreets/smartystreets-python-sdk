class Response:
    def __init__(self, obj):
        self.smarty_key = obj.get('smarty_key', None)
        data_set_name = None
        data_subset_name = None
        if 'data_set_name' in obj:
            self.data_set_name = obj.get('data_set_name')
            data_set_name = obj.get('data_set_name')
        elif 'secondaries' in obj:
            data_set_name = 'secondary'

        if 'data_subset_name' in obj:
            self.data_subset_name = obj.get('data_subset_name', None)
            data_subset_name = obj.get('data_subset_name', None)
        elif 'count' in obj:
            data_set_name = 'secondary'
            data_subset_name = 'count'
            
        if data_set_name == 'secondary':
            if data_subset_name == 'count':
                self.count = obj.get('count', None)
            else:
                self.root_address = get_secondary_root_address(obj.get('root_address', None))
                if 'aliases' in obj:
                    self.aliases = get_secondary_aliases(obj.get('aliases', None))
                self.secondaries = get_secondary_secondaries(obj.get('secondaries', None))
        else:
            self.attributes = get_attributes(data_set_name, data_subset_name, obj.get('attributes', None))

    def __str__(self):
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += get_lines(key, val)
        return '\n    '.join(lines)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, type(self)) and __value.smarty_key == self.smarty_key

def get_lines(key, val):
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

def get_attributes(dataset, data_subset, attribute_obj):
    if dataset == "property":
        if data_subset == "financial":
            return FinancialAttributes(attribute_obj)
        if data_subset == "principal":
            return PrincipalAttributes(attribute_obj)
    if dataset == "geo-reference":
        return GeoReferenceOutputCategories(attribute_obj)

class PrincipalAttributes:
    def __init__(self, obj):
        self.first_floor_sqft = obj.get('1st_floor_sqft', None)
        self.second_floor_sqft = obj.get('2nd_floor_sqft', None)
        self.acres = obj.get('acres', None)
        self.air_conditioner = obj.get('air_conditioner', None)
        self.arbor_pergola = obj.get('arbor_pergola', None)
        self.assessed_improvement_percent = obj.get('assessed_improvement_percent', None)
        self.assessed_improvement_value = obj.get('assessed_improvement_value', None)
        self.assessed_land_value = obj.get('assessed_land_value', None)
        self.assessed_value = obj.get('assessed_value', None)
        self.assessor_last_update = obj.get('assessor_last_update', None)
        self.assessor_taxroll_update = obj.get('assessor_taxroll_update', None)
        self.attic_area = obj.get('attic_area', None)
        self.attic_flag = obj.get('attic_flag', None)
        self.balcony = obj.get('balcony', None)
        self.balcony_area = obj.get('balcony_area', None)
        self.basement_sqft = obj.get('basement_sqft', None)
        self.basement_sqft_finished = obj.get('basement_sqft_finished', None)
        self.basement_sqft_unfinished = obj.get('basement_sqft_unfinished', None)
        self.bath_house = obj.get('bath_house', None)
        self.bath_house_sqft = obj.get('bath_house_sqft', None)
        self.bathrooms_partial = obj.get('bathrooms_partial', None)
        self.bathrooms_total = obj.get('bathrooms_total', None)
        self.bedrooms = obj.get('bedrooms', None)
        self.block1 = obj.get('block1', None)
        self.block2 = obj.get('block2', None)
        self.boat_access = obj.get('boat_access', None)
        self.boat_house = obj.get('boat_house', None)
        self.boat_house_sqft = obj.get('boat_house_sqft', None)
        self.boat_lift = obj.get('boat_lift', None)
        self.bonus_room = obj.get('bonus_room', None)
        self.breakfast_nook = obj.get('breakfast_nook', None)
        self.breezeway = obj.get('breezeway', None)
        self.building_definition_code = obj.get('building_definition_code', None)
        self.building_sqft = obj.get('building_sqft', None)
        self.cabin = obj.get('cabin', None)
        self.cabin_sqft = obj.get('cabin_sqft', None)
        self.canopy = obj.get('canopy', None)
        self.canopy_sqft = obj.get('canopy_sqft', None)
        self.carport = obj.get('carport', None)
        self.carport_sqft = obj.get('carport_sqft', None)
        self.cbsa_code = obj.get('cbsa_code', None)
        self.cbsa_name = obj.get('cbsa_name', None)
        self.cellar = obj.get('cellar', None)
        self.census_block = obj.get('census_block', None)
        self.census_block_group = obj.get('census_block_group', None)
        self.census_fips_place_code = obj.get('census_fips_place_code', None)
        self.census_tract = obj.get('census_tract', None)
        self.central_vacuum = obj.get('central_vacuum', None)
        self.code_title_company = obj.get('code_title_company', None)
        self.combined_statistical_area = obj.get('combined_statistical_area', None)
        self.community_rec = obj.get('community_rec', None)
        self.company_flag = obj.get('company_flag', None)
        self.congressional_district = obj.get('congressional_district', None)
        self.contact_city = obj.get('contact_city', None)
        self.contact_crrt = obj.get('contact_crrt', None)
        self.contact_full_address = obj.get('contact_full_address', None)
        self.contact_house_number = obj.get('contact_house_number', None)
        self.contact_mail_info_format = obj.get('contact_mail_info_format', None)
        self.contact_mail_info_privacy = obj.get('contact_mail_info_privacy', None)
        self.contact_mailing_county = obj.get('contact_mailing_county', None)
        self.contact_mailing_fips = obj.get('contact_mailing_fips', None)
        self.contact_post_direction = obj.get('contact_post_direction', None)
        self.contact_pre_direction = obj.get('contact_pre_direction', None)
        self.contact_state = obj.get('contact_state', None)
        self.contact_street_name = obj.get('contact_street_name', None)
        self.contact_suffix = obj.get('contact_suffix', None)
        self.contact_unit_designator = obj.get('contact_unit_designator', None)
        self.contact_value = obj.get('contact_value', None)
        self.contact_zip = obj.get('contact_zip', None)
        self.contact_zip4 = obj.get('contact_zip4', None)
        self.courtyard = obj.get('courtyard', None)
        self.courtyard_area = obj.get('courtyard_area', None)
        self.deck = obj.get('deck', None)
        self.deck_area = obj.get('deck_area', None)
        self.deed_document_page = obj.get('deed_document_page', None)
        self.deed_document_book = obj.get('deed_document_book', None)
        self.deed_document_number = obj.get('deed_document_number', None)
        self.deed_owner_first_name = obj.get('deed_owner_first_name', None)
        self.deed_owner_first_name2 = obj.get('deed_owner_first_name2', None)
        self.deed_owner_first_name3 = obj.get('deed_owner_first_name3', None)
        self.deed_owner_first_name4 = obj.get('deed_owner_first_name4', None)
        self.deed_owner_full_name = obj.get('deed_owner_full_name', None)
        self.deed_owner_full_name2 = obj.get('deed_owner_full_name2', None)
        self.deed_owner_full_name3 = obj.get('deed_owner_full_name3', None)
        self.deed_owner_full_name4 = obj.get('deed_owner_full_name4', None)
        self.deed_owner_last_name = obj.get('deed_owner_last_name', None)
        self.deed_owner_last_name2 = obj.get('deed_owner_last_name2', None)
        self.deed_owner_last_name3 = obj.get('deed_owner_last_name3', None)
        self.deed_owner_last_name4 = obj.get('deed_owner_last_name4', None)
        self.deed_owner_middle_name = obj.get('deed_owner_middle_name', None)
        self.deed_owner_middle_name = obj.get('deed_owner_middle_name', None)
        self.deed_owner_middle_name2 = obj.get('deed_owner_middle_name2', None)
        self.deed_owner_middle_name3 = obj.get('deed_owner_middle_name3', None)
        self.deed_owner_middle_name4 = obj.get('deed_owner_middle_name4', None)
        self.deed_owner_suffix = obj.get('deed_owner_suffix', None)
        self.deed_owner_suffix2 = obj.get('deed_owner_suffix2', None)
        self.deed_owner_suffix3 = obj.get('deed_owner_suffix3', None)
        self.deed_owner_suffix4 = obj.get('deed_owner_suffix4', None)
        self.deed_sale_date = obj.get('deed_sale_date', None)
        self.deed_sale_price = obj.get('deed_sale_price', None)
        self.deed_transaction_id = obj.get('deed_transaction_id', None)
        self.depth_linear_footage = obj.get('depth_linear_footage', None)
        self.disabled_tax_exemption = obj.get('disabled_tax_exemption', None)
        self.document_type_description = obj.get('document_type_description', None)
        self.driveway_sqft = obj.get('driveway_sqft', None)
        self.driveway_type = obj.get('driveway_type', None)
        self.effective_year_built = obj.get('effective_year_built', None)
        self.elevation_feet = obj.get('elevation_feet', None)
        self.elevator = obj.get('elevator', None)
        self.equestrian_arena = obj.get('equestrian_arena', None)
        self.escalator = obj.get('escalator', None)
        self.exercise_room = obj.get('exercise_room', None)
        self.exterior_walls = obj.get('exterior_walls', None)
        self.family_room = obj.get('family_room', None)
        self.fence = obj.get('fence', None)
        self.fence_area = obj.get('fence_area', None)
        self.fips_code = obj.get('fips_code', None)
        self.fire_resistance_code = obj.get('fire_resistance_code', None)
        self.fire_sprinklers_flag = obj.get('fire_sprinklers_flag', None)
        self.fireplace = obj.get('fireplace', None)
        self.fireplace_number = obj.get('fireplace_number', None)
        self.first_name = obj.get('first_name', None)
        self.first_name_2 = obj.get('first_name_2', None)
        self.first_name_3 = obj.get('first_name_3', None)
        self.first_name_4 = obj.get('first_name_4', None)
        self.flooring = obj.get('flooring', None)
        self.foundation = obj.get('foundation', None)
        self.game_room = obj.get('game_room', None)
        self.garage = obj.get('garage', None)
        self.garage_sqft = obj.get('garage_sqft', None)
        self.gazebo = obj.get('gazebo', None)
        self.gazebo_sqft = obj.get('gazebo_sqft', None)
        self.golf_course = obj.get('golf_course', None)
        self.grainery = obj.get('grainery', None)
        self.grainery_sqft = obj.get('grainery_sqft', None)
        self.great_room = obj.get('great_room', None)
        self.greenhouse = obj.get('greenhouse', None)
        self.greenhouse_sqft = obj.get('greenhouse_sqft', None)
        self.gross_sqft = obj.get('gross_sqft', None)
        self.guesthouse = obj.get('guesthouse', None)
        self.guesthouse_sqft = obj.get('guesthouse_sqft', None)
        self.handicap_accessibility = obj.get('handicap_accessibility', None)
        self.heat = obj.get('heat', None)
        self.heat_fuel_type = obj.get('heat_fuel_type', None)
        self.hobby_room = obj.get('hobby_room', None)
        self.homeowner_tax_exemption = obj.get('homeowner_tax_exemption', None)
        self.instrument_date = obj.get('instrument_date', None)
        self.intercom_system = obj.get('intercom_system', None)
        self.interest_rate_type_2 = obj.get('interest_rate_type_2', None)
        self.interior_structure = obj.get('interior_structure', None)
        self.kennel = obj.get('kennel', None)
        self.kennel_sqft = obj.get('kennel_sqft', None)
        self.land_use_code = obj.get('land_use_code', None)
        self.land_use_group = obj.get('land_use_group', None)
        self.land_use_standard = obj.get('land_use_standard', None)
        self.last_name = obj.get('last_name', None)
        self.last_name_2 = obj.get('last_name_2', None)
        self.last_name_3 = obj.get('last_name_3', None)
        self.last_name_4 = obj.get('last_name_4', None)
        self.latitude = obj.get('latitude', None)
        self.laundry = obj.get('laundry', None)
        self.lean_to = obj.get('lean_to', None)
        self.lean_to_sqft = obj.get('lean_to_sqft', None)
        self.legal_description = obj.get('legal_description', None)
        self.legal_unit = obj.get('legal_unit', None)
        self.lender_address = obj.get('lender_address', None)
        self.lender_address_2 = obj.get('lender_address_2', None)
        self.lender_city = obj.get('lender_city', None)
        self.lender_city_2 = obj.get('lender_city_2', None)
        self.lender_code_2 = obj.get('lender_code_2', None)
        self.lender_first_name = obj.get('lender_first_name', None)
        self.lender_first_name_2 = obj.get('lender_first_name_2', None)
        self.lender_last_name = obj.get('lender_last_name', None)
        self.lender_last_name_2 = obj.get('lender_last_name_2', None)
        self.lender_name = obj.get('lender_name', None)
        self.lender_name_2 = obj.get('lender_name_2', None)
        self.lender_seller_carry_back = obj.get('lender_seller_carry_back', None)
        self.lender_seller_carry_back_2 = obj.get('lender_seller_carry_back_2', None)
        self.lender_state = obj.get('lender_state', None)
        self.lender_state_2 = obj.get('lender_state_2', None)
        self.lender_zip = obj.get('lender_zip', None)
        self.lender_zip_2 = obj.get('lender_zip_2', None)
        self.lender_zip_extended = obj.get('lender_zip_extended', None)
        self.lender_zip_extended_2 = obj.get('lender_zip_extended_2', None)
        self.loading_platform = obj.get('loading_platform', None)
        self.loading_platform_sqft = obj.get('loading_platform_sqft', None)
        self.longitude = obj.get('longitude', None)
        self.lot_1 = obj.get('lot_1', None)
        self.lot_2 = obj.get('lot_2', None)
        self.lot_3 = obj.get('lot_3', None)
        self.lot_sqft = obj.get('lot_sqft', None)
        self.market_improvement_percent = obj.get('market_improvement_percent', None)
        self.market_improvement_value = obj.get('market_improvement_value', None)
        self.market_land_value = obj.get('market_land_value', None)
        self.market_value_year = obj.get('market_value_year', None)
        self.match_type = obj.get('match_type', None)
        self.media_room = obj.get('media_room', None)
        self.metro_division = obj.get('metro_division', None)
        self.middle_name = obj.get('middle_name', None)
        self.middle_name_2 = obj.get('middle_name_2', None)
        self.middle_name_3 = obj.get('middle_name_3', None)
        self.middle_name_4 = obj.get('middle_name_4', None)
        self.milkhouse = obj.get('milkhouse', None)
        self.milkhouse_sqft = obj.get('milkhouse_sqft', None)
        self.minor_civil_division_code = obj.get('minor_civil_division_code', None)
        self.minor_civil_division_name = obj.get('minor_civil_division_name', None)
        self.mobile_home_hookup = obj.get('mobile_home_hookup', None)
        self.mortgage_amount = obj.get('mortgage_amount', None)
        self.mortgage_amount_2 = obj.get('mortgage_amount_2', None)
        self.mortgage_due_date = obj.get('mortgage_due_date', None)
        self.mortgage_due_date_2 = obj.get('mortgage_due_date_2', None)
        self.mortgage_interest_rate = obj.get('mortgage_interest_rate', None)
        self.mortgage_interest_rate_type = obj.get('mortgage_interest_rate_type', None)
        self.mortgage_lender_code = obj.get('mortgage_lender_code', None)
        self.mortgage_rate_2 = obj.get('mortgage_rate_2', None)
        self.mortgage_recording_date = obj.get('mortgage_recording_date', None)
        self.mortgage_recording_date_2 = obj.get('mortgage_recording_date_2', None)
        self.mortgage_term = obj.get('mortgage_term', None)
        self.mortgage_term_2 = obj.get('mortgage_term_2', None)
        self.mortgage_term_type = obj.get('mortgage_term_type', None)
        self.mortgage_term_type_2 = obj.get('mortgage_term_type_2', None)
        self.mortgage_type = obj.get('mortgage_type', None)
        self.mortgage_type_2 = obj.get('mortgage_type_2', None)
        self.msa_code = obj.get('msa_code', None)
        self.msa_name = obj.get('msa_name', None)
        self.mud_room = obj.get('mud_room', None)
        self.multi_parcel_flag = obj.get('multi_parcel_flag', None)
        self.name_title_company = obj.get('name_title_company', None)
        self.neighborhood_code = obj.get('neighborhood_code', None)
        self.number_of_buildings = obj.get('number_of_buildings', None)
        self.office = obj.get('office', None)
        self.office_sqft = obj.get('office_sqft', None)
        self.other_tax_exemption = obj.get('other_tax_exemption', None)
        self.outdoor_kitchen_fireplace = obj.get('outdoor_kitchen_fireplace', None)
        self.overhead_door = obj.get('overhead_door', None)
        self.owner_full_name = obj.get('owner_full_name', None)
        self.owner_full_name_2 = obj.get('owner_full_name_2', None)
        self.owner_full_name_3 = obj.get('owner_full_name_3', None)
        self.owner_full_name_4 = obj.get('owner_full_name_4', None)
        self.owner_occupancy_status = obj.get('owner_occupancy_status', None)
        self.ownership_transfer_date = obj.get('ownership_transfer_date', None)
        self.ownership_transfer_doc_number = obj.get('ownership_transfer_doc_number', None)
        self.ownership_transfer_transaction_id = obj.get('ownership_transfer_transaction_id', None)
        self.ownership_type = obj.get('ownership_type', None)
        self.ownership_type_2 = obj.get('ownership_type_2', None)
        self.ownership_vesting_relation_code = obj.get('ownership_vesting_relation_code', None)
        self.parcel_account_number = obj.get('parcel_account_number', None)
        self.parcel_map_book = obj.get('parcel_map_book', None)
        self.parcel_map_page = obj.get('parcel_map_page', None)
        self.parcel_number_alternate = obj.get('parcel_number_alternate', None)
        self.parcel_number_formatted = obj.get('parcel_number_formatted', None)
        self.parcel_number_previous = obj.get('parcel_number_previous', None)
        self.parcel_number_year_added = obj.get('parcel_number_year_added', None)
        self.parcel_number_year_change = obj.get('parcel_number_year_change', None)
        self.parcel_raw_number = obj.get('parcel_raw_number', None)
        self.parcel_shell_record = obj.get('parcel_shell_record', None)
        self.parking_spaces = obj.get('parking_spaces', None)
        self.patio_area = obj.get('patio_area', None)
        self.phase_name = obj.get('phase_name', None)
        self.plumbing_fixtures_count = obj.get('plumbing_fixtures_count', None)
        self.pole_struct = obj.get('pole_struct', None)
        self.pole_struct_sqft = obj.get('pole_struct_sqft', None)
        self.pond = obj.get('pond', None)
        self.pool = obj.get('pool', None)
        self.pool_area = obj.get('pool_area', None)
        self.poolhouse = obj.get('poolhouse', None)
        self.poolhouse_sqft = obj.get('poolhouse_sqft', None)
        self.porch = obj.get('porch', None)
        self.porch_area = obj.get('porch_area', None)
        self.poultry_house = obj.get('poultry_house', None)
        self.poultry_house_sqft = obj.get('poultry_house_sqft', None)
        self.previous_assessed_value = obj.get('previous_assessed_value', None)
        self.prior_sale_amount = obj.get('prior_sale_amount', None)
        self.prior_sale_date = obj.get('prior_sale_date', None)
        self.property_address_carrier_route_code = obj.get('property_address_carrier_route_code', None)
        self.property_address_city = obj.get('property_address_city', None)
        self.property_address_full = obj.get('property_address_full', None)
        self.property_address_house_number = obj.get('property_address_house_number', None)
        self.property_address_post_direction = obj.get('property_address_post_direction', None)
        self.property_address_pre_direction = obj.get('property_address_pre_direction', None)
        self.property_address_state = obj.get('property_address_state', None)
        self.property_address_street_name = obj.get('property_address_street_name', None)
        self.property_address_street_suffix = obj.get('property_address_street_suffix', None)
        self.property_address_unit_designator = obj.get('property_address_unit_designator', None)
        self.property_address_unit_value = obj.get('property_address_unit_value', None)
        self.property_address_zip_4 = obj.get('property_address_zip_4', None)
        self.property_address_zipcode = obj.get('property_address_zipcode', None)
        self.publication_date = obj.get('publication_date', None)
        self.quarter = obj.get('quarter', None)
        self.quarter_quarter = obj.get('quarter_quarter', None)
        self.quonset = obj.get('quonset', None)
        self.quonset_sqft = obj.get('quonset_sqft', None)
        self.range = obj.get('range', None)
        self.recording_date = obj.get('recording_date', None)
        self.roof_cover = obj.get('roof_cover', None)
        self.roof_frame = obj.get('roof_frame', None)
        self.rooms = obj.get('rooms', None)
        self.rv_parking = obj.get('rv_parking', None)
        self.safe_room = obj.get('safe_room', None)
        self.sale_amount = obj.get('sale_amount', None)
        self.sale_date = obj.get('sale_date', None)
        self.sauna = obj.get('sauna', None)
        self.section = obj.get('section', None)
        self.security_alarm = obj.get('security_alarm', None)
        self.senior_tax_exemption = obj.get('senior_tax_exemption', None)
        self.sewer_type = obj.get('sewer_type', None)
        self.shed = obj.get('shed', None)
        self.shed_sqft = obj.get('shed_sqft', None)
        self.silo = obj.get('silo', None)
        self.silo_sqft = obj.get('silo_sqft', None)
        self.sitting_room = obj.get('sitting_room', None)
        self.situs_county = obj.get('situs_county', None)
        self.situs_state = obj.get('situs_state', None)
        self.sound_system = obj.get('sound_system', None)
        self.sports_court = obj.get('sports_court', None)
        self.sprinklers = obj.get('sprinklers', None)
        self.stable = obj.get('stable', None)
        self.stable_sqft = obj.get('stable_sqft', None)
        self.storage_building = obj.get('storage_building', None)
        self.storage_building_sqft = obj.get('storage_building_sqft', None)
        self.stories_number = obj.get('stories_number', None)
        self.storm_shelter = obj.get('storm_shelter', None)
        self.storm_shutter = obj.get('storm_shutter', None)
        self.structure_style = obj.get('structure_style', None)
        self.study = obj.get('study', None)
        self.subdivision = obj.get('subdivision', None)
        self.suffix = obj.get('suffix', None)
        self.suffix_2 = obj.get('suffix_2', None)
        self.suffix_3 = obj.get('suffix_3', None)
        self.suffix_4 = obj.get('suffix_4', None)
        self.sunroom = obj.get('sunroom', None)
        self.tax_assess_year = obj.get('tax_assess_year', None)
        self.tax_billed_amount = obj.get('tax_billed_amount', None)
        self.tax_delinquent_year = obj.get('tax_delinquent_year', None)
        self.tax_fiscal_year = obj.get('tax_fiscal_year', None)
        self.tax_jurisdiction = obj.get('tax_jurisdiction', None)
        self.tax_rate_area = obj.get('tax_rate_area', None)
        self.tennis_court = obj.get('tennis_court', None)
        self.topography_code = obj.get('topography_code', None)
        self.total_market_value = obj.get('total_market_value', None)
        self.township = obj.get('township', None)
        self.tract_number = obj.get('tract_number', None)
        self.transfer_amount = obj.get('transfer_amount', None)
        self.trust_description = obj.get('trust_description', None)
        self.unit_count = obj.get('unit_count', None)
        self.upper_floors_sqft = obj.get('upper_floors_sqft', None)
        self.utility = obj.get('utility', None)
        self.utility_building = obj.get('utility_building', None)
        self.utility_building_sqft = obj.get('utility_building_sqft', None)
        self.utility_sqft = obj.get('utility_sqft', None)
        self.veteran_tax_exemption = obj.get('veteran_tax_exemption', None)
        self.view_description = obj.get('view_description', None)
        self.water_feature = obj.get('water_feature', None)
        self.water_service_type = obj.get('water_service_type', None)
        self.wet_bar = obj.get('wet_bar', None)
        self.widow_tax_exemption = obj.get('widow_tax_exemption', None)
        self.width_linear_footage = obj.get('width_linear_footage', None)
        self.wine_cellar = obj.get('wine_cellar', None)
        self.year_built = obj.get('year_built', None)
        self.zoning = obj.get('zoning', None)

    def __str__(self):
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


class FinancialAttributes:
    def __init__(self, obj):
        self.assessed_improvement_percent = obj.get('assessed_improvement_percent', None)
        self.assessed_improvement_value = obj.get('assessed_improvement_value', None)
        self.assessed_land_value = obj.get('assessed_land_value', None)
        self.assessed_value = obj.get('assessed_value', None)
        self.assessor_last_update = obj.get('assessor_last_update', None)
        self.assessor_taxroll_update = obj.get('assessor_taxroll_update', None)
        self.contact_city = obj.get('contact_city', None)
        self.contact_crrt = obj.get('contact_crrt', None)
        self.contact_full_address = obj.get('contact_full_address', None)
        self.contact_house_number = obj.get('contact_house_number', None)
        self.contact_mail_info_format = obj.get('contact_mail_info_format', None)
        self.contact_mail_info_privacy = obj.get('contact_mail_info_privacy', None)
        self.contact_mailing_county = obj.get('contact_mailing_county', None)
        self.contact_mailing_fips = obj.get('contact_mailing_fips', None)
        self.contact_post_direction = obj.get('contact_post_direction', None)
        self.contact_pre_direction = obj.get('contact_pre_direction', None)
        self.contact_state = obj.get('contact_state', None)
        self.contact_street_name = obj.get('contact_street_name', None)
        self.contact_suffix = obj.get('contact_suffix', None)
        self.contact_unit_designator = obj.get('contact_unit_designator', None)
        self.contact_value = obj.get('contact_value', None)
        self.contact_zip = obj.get('contact_zip', None)
        self.contact_zip4 = obj.get('contact_zip4', None)
        self.deed_document_page = obj.get('deed_document_page', None)
        self.deed_document_book = obj.get('deed_document_book', None)
        self.deed_document_number = obj.get('deed_document_number', None)
        self.deed_owner_first_name = obj.get('deed_owner_first_name', None)
        self.deed_owner_first_name2 = obj.get('deed_owner_first_name2', None)
        self.deed_owner_first_name3 = obj.get('deed_owner_first_name3', None)
        self.deed_owner_first_name4 = obj.get('deed_owner_first_name4', None)
        self.deed_owner_full_name = obj.get('deed_owner_full_name', None)
        self.deed_owner_full_name2 = obj.get('deed_owner_full_name2', None)
        self.deed_owner_full_name3 = obj.get('deed_owner_full_name3', None)
        self.deed_owner_full_name4 = obj.get('deed_owner_full_name4', None)
        self.deed_owner_last_name = obj.get('deed_owner_last_name', None)
        self.deed_owner_last_name2 = obj.get('deed_owner_last_name2', None)
        self.deed_owner_last_name3 = obj.get('deed_owner_last_name3', None)
        self.deed_owner_last_name4 = obj.get('deed_owner_last_name4', None)
        self.deed_owner_middle_name = obj.get('deed_owner_middle_name', None)
        self.deed_owner_middle_name2 = obj.get('deed_owner_middle_name2', None)
        self.deed_owner_middle_name3 = obj.get('deed_owner_middle_name3', None)
        self.deed_owner_middle_name4 = obj.get('deed_owner_middle_name4', None)
        self.deed_owner_suffix = obj.get('deed_owner_suffix', None)
        self.deed_owner_suffix2 = obj.get('deed_owner_suffix2', None)
        self.deed_owner_suffix3 = obj.get('deed_owner_suffix3', None)
        self.deed_owner_suffix4 = obj.get('deed_owner_suffix4', None)
        self.deed_sale_date = obj.get('deed_sale_date', None)
        self.deed_sale_price = obj.get('deed_sale_price', None)
        self.deed_transaction_id = obj.get('deed_transaction_id', None)
        self.disabled_tax_exemption = obj.get('disabled_tax_exemption', None)
        self.financial_history = get_financial_history(obj.get('financial_history', None))
        self.first_name = obj.get('first_name', None)
        self.first_name_2 = obj.get('first_name_2', None)
        self.first_name_3 = obj.get('first_name_3', None)
        self.first_name_4 = obj.get('first_name_4', None)
        self.homeowner_tax_exemption = obj.get('homeowner_tax_exemption', None)
        self.last_name= obj.get('last_name', None)
        self.last_name_2 = obj.get('last_name_2', None)
        self.last_name_3 = obj.get('last_name_3', None)
        self.last_name_4 = obj.get('last_name_4', None)
        self.market_improvement_percent = obj.get('market_improvement_percent', None)
        self.market_improvement_value = obj.get('market_improvement_value', None)
        self.market_land_value = obj.get('market_land_value', None)
        self.market_value_year = obj.get('market_value_year', None)
        self.match_type = obj.get('match_type', None)
        self.middle_name= obj.get('middle_name', None)
        self.middle_name_2 = obj.get('middle_name_2', None)
        self.middle_name_3 = obj.get('middle_name_3', None)
        self.middle_name_4 = obj.get('middle_name_4', None)
        self.other_tax_exemption = obj.get('other_tax_exemption', None)
        self.owner_full_name = obj.get('owner_full_name', None)
        self.owner_full_name_2 = obj.get('owner_full_name_2', None)
        self.owner_full_name_3 = obj.get('owner_full_name_3', None)
        self.owner_full_name_4 = obj.get('owner_full_name_4', None)
        self.ownership_transfer_date = obj.get('ownership_transfer_date', None)
        self.ownership_transfer_doc_number = obj.get('ownership_transfer_doc_number', None)
        self.ownership_transfer_transaction_id = obj.get('ownership_transfer_transaction_id', None)
        self.ownership_type = obj.get('ownership_type', None)
        self.ownership_type_2 = obj.get('ownership_type_2', None)
        self.previous_assessed_value = obj.get('previous_assessed_value', None)
        self.prior_sale_amount = obj.get('prior_sale_amount', None)
        self.prior_sale_date = obj.get('prior_sale_date', None)
        self.sale_amount = obj.get('sale_amount', None)
        self.sale_date = obj.get('sale_date', None)
        self.senior_tax_exemption = obj.get('senior_tax_exemption', None)
        self.suffix = obj.get('suffix', None)
        self.suffix_2 = obj.get('suffix_2', None)
        self.suffix_3 = obj.get('suffix_3', None)
        self.suffix_4 = obj.get('suffix_4', None)
        self.tax_assess_year = obj.get('tax_assess_year', None)
        self.tax_billed_amount = obj.get('tax_billed_amount', None)
        self.tax_delinquent_year = obj.get('tax_delinquent_year', None)
        self.tax_fiscal_year = obj.get('tax_fiscal_year', None)
        self.tax_rate_area = obj.get('tax_rate_area', None)
        self.total_market_value = obj.get('total_market_value', None)
        self.trust_description = obj.get('trust_description', None)
        self.veteran_tax_exemption = obj.get('veteran_tax_exemption', None)
        self.widow_tax_exemption = obj.get('widow_tax_exemption', None)

    def __str__(self):
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


def get_financial_history(financial_history_obj):
    if financial_history_obj is None:
        return None
    output = []
    for obj in financial_history_obj:
        output.append(FinancialHistory(obj))
    return output


class FinancialHistory:
    def __init__(self, obj):
        self.code_title_company = obj.get('code_title_company', None)
        self.document_type_description = obj.get('document_type_description', None)
        self.instrument_date = obj.get('instrument_date', None)
        self.interest_rate_type_2 = obj.get('interest_rate_type_2', None)
        self.lender_address = obj.get('lender_address', None)
        self.lender_address_2 = obj.get('lender_address_2', None)
        self.lender_city = obj.get('lender_city', None)
        self.lender_city_2 = obj.get('lender_city_2', None)
        self.lender_code_2 = obj.get('lender_code_2', None)
        self.lender_first_name = obj.get('lender_first_name', None)
        self.lender_first_name_2 = obj.get('lender_first_name_2', None)
        self.lender_last_name = obj.get('lender_last_name', None)
        self.lender_last_name_2 = obj.get('lender_last_name_2', None)
        self.lender_name = obj.get('lender_name', None)
        self.lender_name_2 = obj.get('lender_name_2', None)
        self.lender_seller_carry_back = obj.get('lender_seller_carry_back', None)
        self.lender_seller_carry_back_2 = obj.get('lender_seller_carry_back_2', None)
        self.lender_state = obj.get('lender_state', None)
        self.lender_state_2 = obj.get('lender_state_2', None)
        self.lender_zip = obj.get('lender_zip', None)
        self.lender_zip_2 = obj.get('lender_zip_2', None)
        self.lender_zip_extended = obj.get('lender_zip_extended', None)
        self.lender_zip_extended_2 = obj.get('lender_zip_extended_2', None)
        self.mortgage_amount = obj.get('mortgage_amount', None)
        self.mortgage_amount_2 = obj.get('mortgage_amount_2', None)
        self.mortgage_due_date = obj.get('mortgage_due_date', None)
        self.mortgage_due_date_2 = obj.get('mortgage_due_date_2', None)
        self.mortgage_interest_rate = obj.get('mortgage_interest_rate', None)
        self.mortgage_interest_rate_type = obj.get('mortgage_interest_rate_type', None)
        self.mortgage_lender_code = obj.get('mortgage_lender_code', None)
        self.mortgage_rate_2 = obj.get('mortgage_rate_2', None)
        self.mortgage_recording_date = obj.get('mortgage_recording_date', None)
        self.mortgage_recording_date_2 = obj.get('mortgage_recording_date_2', None)
        self.mortgage_term = obj.get('mortgage_term', None)
        self.mortgage_term_2 = obj.get('mortgage_term_2', None)
        self.mortgage_term_type = obj.get('mortgage_term_type', None)
        self.mortgage_term_type_2 = obj.get('mortgage_term_type_2', None)
        self.mortgage_type = obj.get('mortgage_type', None)
        self.mortgage_type_2 = obj.get('mortgage_type_2', None)
        self.multi_parcel_flag = obj.get('multi_parcel_flag', None)
        self.name_title_company = obj.get('name_title_company', None)
        self.recording_date = obj.get('recording_date', None)
        self.transfer_amount = obj.get('transfer_amount', None)

    def __str__(self):
        return self.__dict__.__str__()
    
class GeoReferenceOutputCategories:
    def __init__(self, obj):
        
        self.census_block = get_geo_reference_census_block(obj.get('census_block', None))
        self.census_county_division = get_geo_reference_census_county_division(obj.get('census_county_division', None))
        self.census_tract = get_geo_reference_census_tract(obj.get('census_tract', None))
        self.core_based_stat_area = get_geo_reference_core_based_stat_area(obj.get('core_based_stat_area', None))
        self.place = get_geo_reference_place(obj.get('place', None))

    def __str__(self):
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
    def __init__(self, obj):
        self.accuracy = obj.get('accuracy', None)
        self.geoid = obj.get('geoid', None)

    def __str__(self):
        return self.__dict__.__str__()
    
def get_geo_reference_census_block(geo_reference_census_block_obj):
    if geo_reference_census_block_obj is None:
        return None
    output = []
    output.append(GeoReferenceCensusBlock(geo_reference_census_block_obj))
    return output

class GeoReferenceCensusCountyDivision:
    def __init__(self, obj):
        self.accuracy = obj.get('accuracy', None)
        self.code = obj.get('code', None)
        self.name = obj.get('name', None)

    def __str__(self):
        return self.__dict__.__str__()
    
def get_geo_reference_census_county_division(geo_reference_census_county_division_obj):
    if geo_reference_census_county_division_obj is None:
        return None
    output = []
    output.append(GeoReferenceCensusCountyDivision(geo_reference_census_county_division_obj))
    return output

class GeoReferenceCensusTract:
    def __init__(self, obj):
        self.code = obj.get('code', None)

    def __str__(self):
        return self.__dict__.__str__()
    
def get_geo_reference_census_tract(geo_reference_census_tract_obj):
    if geo_reference_census_tract_obj is None:
        return None
    output = []
    output.append(GeoReferenceCensusTract(geo_reference_census_tract_obj))
    return output

class GeoReferenceCoreBasedStatArea:
    def __init__(self, obj):
        self.code = obj.get('code', None)
        self.name = obj.get('name', None)

    def __str__(self):
        return self.__dict__.__str__()
    
def get_geo_reference_core_based_stat_area(geo_reference_core_based_stat_area_obj):
    if geo_reference_core_based_stat_area_obj is None:
        return None
    output = []
    output.append(GeoReferenceCoreBasedStatArea(geo_reference_core_based_stat_area_obj))
    return output

class GeoReferencePlace:
    def __init__(self, obj):
        self.accuracy = obj.get('accuracy', None)
        self.code = obj.get('code', None)
        self.name = obj.get('name', None)
        self.type = obj.get('type', None)

    def __str__(self):
        return self.__dict__.__str__()

def get_geo_reference_place(geo_reference_place_obj):
    if geo_reference_place_obj is None:
        return None
    output = []
    output.append(GeoReferencePlace(geo_reference_place_obj))
    return output

class SecondaryRootAddress:
    def __init__(self, obj):
        self.secondary_count = obj.get('secondary_count', None)
        self.smarty_key = obj.get('smarty_key', None)
        self.primary_number = obj.get('primary_number', None)
        self.street_predirection = obj.get('street_predirection', None)
        self.street_name = obj.get('street_name', None)
        self.street_suffix = obj.get('street_suffix', None)
        self.street_postdirection = obj.get('street_postdirection', None)
        self.city_name = obj.get('city_name', None)
        self.state_abbreviation = obj.get('state_abbreviation', None)
        self.zipcode = obj.get('zipcode', None)
        self.plus4_code = obj.get('plus4_code', None)

    def __str__(self):
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

def get_secondary_root_address(secondary_root_address_obj):
    if secondary_root_address_obj is None:
        return None
    output = []
    output.append(SecondaryRootAddress(secondary_root_address_obj))

    return output

class SecondaryAliases:
    def __init__(self, obj):
        self.smarty_key = obj.get('smarty_key', None)
        self.primary_number = obj.get('primary_number', None)
        self.street_predirection = obj.get('street_predirection', None)
        self.street_name = obj.get('street_name', None)
        self.street_suffix = obj.get('street_suffix', None)
        self.street_postdirection = obj.get('street_postdirection', None)
        self.city_name = obj.get('city_name', None)
        self.state_abbreviation = obj.get('state_abbreviation', None)
        self.zipcode = obj.get('zipcode', None)
        self.plus4_code = obj.get('plus4_code', None)

    def __str__(self):
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

def get_secondary_aliases(secondary_aliases_obj):
    if secondary_aliases_obj is None:
        return None
    output = []
    for item in secondary_aliases_obj:
        output.append(SecondaryAliases(item))
    return output

class SecondarySecondaries:
    def __init__(self, obj):
        self.smarty_key = obj.get('smarty_key', None)
        self.secondary_designator = obj.get('secondary_designator', None)
        self.secondary_number = obj.get('secondary_number', None)
        self.plus4_code = obj.get('plus4_code', None)

    def __str__(self):
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

def get_secondary_secondaries(secondary_secondaries_obj):
    if secondary_secondaries_obj is None:
        return None
    output = []
    for item in secondary_secondaries_obj:
        output.append(SecondarySecondaries(item))
    return output

class SecondaryCountAttributes:
    def __init__(self, obj):
        self.smarty_key = obj.get('smarty_key', None)
        self.count = obj.get('count', None)

    def __str__(self):
        return self.__dict__.__str__()