import psycopg2
from psycopg2.extras import execute_values


class Database:

    def __init__(self, connection, cursor):
        """
        :type connection: psycopg2.extensions.connection
        :type cursor: psycopg2.extensions.cursor
        """

        self._connection = connection
        self._cursor = cursor

    @classmethod
    def connect(cls, connection_uri):
        """"
        :type connection_uri: str
        :rtype: epicollect_migrator.database.Database
        """

        connection = psycopg2.connect(connection_uri)

        return cls(connection, connection.cursor())

    def add_v1_points(self, points):

        sql = """
        INSERT INTO epicollect_observations (
        	uuid,
	        created_at,
	        created_by,
	        title,
	        location_name_desc,
	        water_matters,
	        general_island_area,
	        named_location_if_known,
	        watershed,
	        where_am_i,
	        weather_check_all_that_apply,
	        last_significant_precipitation_event,
	        safe_to_work_at_this_location,
	        name_initials_or_nickname,
	        no_of_participants,
	        type_of_visit,
	        general_land_use_in_area_to_25m,
	        describe_other_land_use,
	        types_of_water_use,
	        describe_other_water_use,
	        this_area_recieve,
	        describe_other_drainage,
	        vegetation_in_area,
	        canopy_coverage_within_5m,
	        soil_rock_type,
	        water_body_type,
	        water_body_name_if_known,
	        water_movement_visible,
	        likely_permenance,
	        flow_measurement_location,
	        describe_other_fl,
	        wetted_width_m,
	        rate_of_flow_qualitative,
	        describe_water_level_qualitative,
	        method_of_measurement,
	        describe_other_measurement,
	        flow_rate_quantity_1,
	        flow_rate_quantity_2,
	        flow_rate_quantity_3,
	        any_of_the_following_on_the_water_surface,
	        type_of_algae_if_present,
	        evidence_of_aquatic_life,
	        describe_other_incidental_species,
	        water_colour_hue,
	        photo_view_upstr,
	        photo_view_downstream,
	        do_you_want_to_take_more_photos,
	        additional_photo_1,
	        additional_photo_2,
	        are_you_taking_water_samples,
	        ph,
	        temperature,
	        conductivity,
	        other_comments
        )
        VALUES %s
        ON CONFLICT (uuid) DO UPDATE SET
            uuid = excluded.uuid,
	        created_at = excluded.created_at,
	        created_by = excluded.created_by,
	        title = excluded.title,
	        location_name_desc = excluded.location_name_desc,
	        water_matters = excluded.water_matters,
	        general_island_area = excluded.general_island_area,
	        named_location_if_known = excluded.named_location_if_known,
	        watershed = excluded.watershed,
	        where_am_i = excluded.where_am_i,
	        weather_check_all_that_apply = excluded.weather_check_all_that_apply,
	        last_significant_precipitation_event = excluded.last_significant_precipitation_event,
	        safe_to_work_at_this_location = excluded.safe_to_work_at_this_location,
	        name_initials_or_nickname = excluded.name_initials_or_nickname,
	        no_of_participants = excluded.no_of_participants,
	        type_of_visit = excluded.type_of_visit,
	        general_land_use_in_area_to_25m = excluded.general_land_use_in_area_to_25m,
	        describe_other_land_use = excluded.describe_other_land_use,
	        types_of_water_use = excluded.types_of_water_use,
	        describe_other_water_use = excluded.describe_other_water_use,
	        this_area_recieve = excluded.this_area_recieve,
	        describe_other_drainage = excluded.describe_other_drainage,
	        vegetation_in_area = excluded.vegetation_in_area,
	        canopy_coverage_within_5m = excluded.canopy_coverage_within_5m,
	        soil_rock_type = excluded.soil_rock_type,
	        water_body_type = excluded.water_body_type,
	        water_body_name_if_known = excluded.water_body_name_if_known,
	        water_movement_visible = excluded.water_movement_visible,
	        likely_permenance = excluded.likely_permenance,
	        flow_measurement_location = excluded.flow_measurement_location,
	        describe_other_fl = excluded.describe_other_fl,
	        wetted_width_m = excluded.wetted_width_m,
	        rate_of_flow_qualitative = excluded.rate_of_flow_qualitative,
	        describe_water_level_qualitative = excluded.describe_water_level_qualitative,
	        method_of_measurement = excluded.method_of_measurement,
	        describe_other_measurement = excluded.describe_other_measurement,
	        flow_rate_quantity_1 = excluded.flow_rate_quantity_1,
	        flow_rate_quantity_2 = excluded.flow_rate_quantity_2,
	        flow_rate_quantity_3 = excluded.flow_rate_quantity_3,
	        any_of_the_following_on_the_water_surface = excluded.any_of_the_following_on_the_water_surface,
	        type_of_algae_if_present = excluded.type_of_algae_if_present,
	        evidence_of_aquatic_life = excluded.evidence_of_aquatic_life,
	        describe_other_incidental_species = excluded.describe_other_incidental_species,
	        water_colour_hue = excluded.water_colour_hue,
	        photo_view_upstr = excluded.photo_view_upstr,
	        photo_view_downstream = excluded.photo_view_downstream,
	        do_you_want_to_take_more_photos = excluded.do_you_want_to_take_more_photos,
	        additional_photo_1 = excluded.additional_photo_1,
	        additional_photo_2 = excluded.additional_photo_2,
	        are_you_taking_water_samples = excluded.are_you_taking_water_samples,
	        ph = excluded.ph,
	        temperature = excluded.temperature,
	        conductivity = excluded.conductivity,
	        other_comments = excluded.other_comments;
        """

        execute_values(self._cursor, sql, points)

    def add_v2_points(self, points):
        sql = """
                INSERT INTO epicollect_observations_v2 (
                    uuid,
                    created_at,
                    created_by,
                    title,
                    LocName,
                    i_am_a_hiker_walker,
                    date,
                    photo,
                    water_body_type,
                    water_movement,
                    brief_description,
                    should_ssifwc_visit,
                    island_area,
                    sub_loc_north,
                    sub_loc_central,
                    sub_loc_south,
                    other_loc_north,
                    other_loc_central,
                    other_loc_south,
                    coord geo,
                    date_2,
                    time_2 ,
                    temp,
                    cloud_cover,
                    precipitation,
                    last_sig_precipitation,
                    safe_to_work,
                    name,
                    number_of_participants,
                    water_moving,
                    flow_type,
                    visit_type,
                    gen_land_use,
                    other_land_use,
                    water_use,
                    other_water_use,
                    drainage_sources,
                    terrain,
                    water_level,
                    vegetation,
                    canopy_coverage,
                    surficial_geology,
                    water_surface,
                    algae,
                    algae_extent,
                    aquatic_life,
                    other_species,
                    absolute_depth_me,
                    describe_location,
                    describe_reference,
                    photo_of_water_le,
                    flow_measure,
                    flow_measure_loc,
                    current_wetted_wi,
                    estimated_wetted,
                    water_color,
                    water_turbitidy_q,
                    type_measure,
                    rate_of_flow,
                    describe_water_level,
                    method_measure,
                    simple_or_detailed,
                    measure_depth_cm,
                    distance_from_ban_1,
                    depth_at_pt_1_cm,
                    distance_from_ban_2,
                    depth_at_pt_2_cm,
                    distance_from_ban_3,
                    depth_at_pt_3_cm,
                    distance_from_ban_4,
                    depth_at_pt_4_cm,
                    distance_from_ban_5,
                    depth_at_pt_5_cm,
                    distance_from_ban_6,
                    depth_at_pt_6_cm,
                    distance_from_ban_7,
                    depth_at_pt_7_cm ,
                    distance_from_ban_8,
                    depth_at_pt_8_cm,
                    distance_from_ban_9,
                    depth_at_pt_9_cm,
                    distance_from_ban_10,
                    depth_at_pt_10_cm,
                    quantitative_meas,
                    velocity_1_ms,
                    velocity_2_ms,
                    velocity_3_ms,
                    depth_to_meter_fr,
                    depth_from_meter,
                    enter_xsection_ar_1,
                    distance_traveled,
                    time_1_sec,
                    time_2_sec,
                    time_3_sec,
                    enter_xsection_ar_2,
                    flow_rate_average,
                    measurement_1_ls,
                    measurement_1_tim,
                    measurement_2_ls,
                    measurement_2_tim,
                    measurement_3_ls,
                    measurement_3_tim,
                    are_you_taking_ph,
                    photos,
                    photo_view_downst,
                    do_you_want_to_ta,
                    additional_photo_1,
                    additional_photo_2,
                    short_video,
                    are_you_taking_wa,
                    ph,
                    temperature,
                    conductivity,
                    total_dissolved,
                    dissolved_oxygen,
                    other_comments
                )
                VALUES %s
                ON CONFLICT (uuid) DO UPDATE SET
                    uuid = excluded.uuid,
                    created_at = excluded.created_at
                    created_by = excluded.created_by
                    title = excluded.title
                    LocName = excluded.LocName
                    i_am_a_hiker_walker = excluded.i_am_a_hiker_walker
                    date = excluded.date
                    photo = excluded.photo
                    water_body_type = excluded.water_body_type
                    water_movement = excluded.water_movement
                    brief_description = excluded.brief_description
                    should_ssifwc_visit = excluded.should_ssifwc_visit
                    island_area = excluded.island_area
                    sub_loc_north = excluded.sub_loc_north
                    sub_loc_central = excluded.sub_loc_central
                    sub_loc_south = excluded.sub_loc_south
                    other_loc_north = excluded.other_loc_north
                    other_loc_central = excluded.other_loc_central
                    other_loc_south = excluded.other_loc_south
                    coord = excluded.coord
                    date_2 = excluded.date_2
                    time_2  = excluded.time_2
                    temp = excluded.temp
                    cloud_cover = excluded.cloud_cover
                    precipitation = excluded.precipitation
                    last_sig_precipitation = excluded.last_sig_precipitation
                    safe_to_work = excluded.safe_to_work
                    name = excluded.name
                    number_of_participants = excluded.number_of_participants
                    water_moving = excluded.water_moving
                    flow_type = excluded.flow_type
                    visit_type = excluded.visit_type
                    gen_land_use = excluded.gen_land_use
                    other_land_use = excluded.other_land_use
                    water_use = excluded.water_use
                    other_water_use = excluded.other_water_use
                    drainage_sources = excluded.drainage_sources
                    terrain = excluded.terrain
                    water_level = excluded.water_level
                    vegetation = excluded.vegetation
                    canopy_coverage = excluded.canopy_coverage
                    surficial_geology = excluded.surficial_geology
                    water_surface = excluded.water_surface
                    algae = excluded.algae
                    algae_extent = excluded.algae_extent
                    aquatic_life = excluded.aquatic_life
                    other_species = excluded.other_species
                    absolute_depth_me = excluded.absolute_depth_me
                    describe_location = excluded.describe_location
                    describe_reference = excluded.describe_reference
                    photo_of_water_le = excluded.photo_of_water_le
                    flow_measure = excluded.flow_measure
                    flow_measure_loc = excluded.flow_measure_loc
                    current_wetted_wi = excluded.current_wetted_wi
                    estimated_wetted = excluded.estimated_wetted
                    water_color = excluded.water_color
                    water_turbitidy_q = excluded.water_turbitidy_q
                    type_measure = excluded.type_measure
                    rate_of_flow = excluded.rate_of_flow
                    describe_water_level = excluded.describe_water_level
                    method_measure = excluded.method_measure
                    simple_or_detailed = excluded.simple_or_detailed
                    measure_depth_cm = excluded.measure_depth_cm
                    distance_from_ban_1 = excluded.distance_from_ban_1
                    depth_at_pt_1_cm = excluded.depth_at_pt_1_cm
                    distance_from_ban_2 = excluded.distance_from_ban_2
                    depth_at_pt_2_cm = excluded.depth_at_pt_2_cm
                    distance_from_ban_3 = excluded.distance_from_ban_3
                    depth_at_pt_3_cm = excluded.depth_at_pt_3_cm
                    distance_from_ban_4 = excluded.distance_from_ban_4
                    depth_at_pt_4_cm = excluded.depth_at_pt_4_cm
                    distance_from_ban_5 = excluded.distance_from_ban_5
                    depth_at_pt_5_cm = excluded.depth_at_pt_5_cm
                    distance_from_ban_6 = excluded.distance_from_ban_6
                    depth_at_pt_6_cm = excluded.depth_at_pt_6_cm
                    distance_from_ban_7 = excluded.distance_from_ban_7
                    depth_at_pt_7_cm  = excluded.depth_at_pt_7_cm
                    distance_from_ban_8 = excluded.distance_from_ban_8
                    depth_at_pt_8_cm = excluded.depth_at_pt_8_cm
                    distance_from_ban_9 = excluded.distance_from_ban_9
                    depth_at_pt_9_cm = excluded.depth_at_pt_9_cm
                    distance_from_ban_10 = excluded.distance_from_ban_10
                    depth_at_pt_10_cm = excluded.depth_at_pt_10_cm
                    quantitative_meas = excluded.quantitative_meas
                    velocity_1_ms = excluded.velocity_1_ms
                    velocity_2_ms = excluded.velocity_2_ms
                    velocity_3_ms = excluded.velocity_3_ms
                    depth_to_meter_fr = excluded.depth_to_meter_fr
                    depth_from_meter = excluded.depth_from_meter
                    enter_xsection_ar_1 = excluded.enter_xsection_ar_1
                    distance_traveled = excluded.distance_traveled
                    time_1_sec = excluded.time_1_sec
                    time_2_sec = excluded.time_2_sec
                    time_3_sec = excluded.time_3_sec
                    enter_xsection_ar_2 = excluded.enter_xsection_ar_2
                    flow_rate_average = excluded.flow_rate_average
                    measurement_1_ls = excluded.measurement_1_ls
                    measurement_1_tim = excluded.measurement_1_tim
                    measurement_2_ls = excluded.measurement_2_ls
                    measurement_2_tim = excluded.measurement_2_tim
                    measurement_3_ls = excluded.measurement_3_ls
                    measurement_3_tim = excluded.measurement_3_tim
                    are_you_taking_ph = excluded.are_you_taking_ph
                    photos = excluded.photos
                    photo_view_downst = excluded.photo_view_downst
                    do_you_want_to_ta = excluded.do_you_want_to_ta
                    additional_photo_1 = excluded.additional_photo_1
                    additional_photo_2 = excluded.additional_photo_2
                    short_video = excluded.short_video
                    are_you_taking_wa = excluded.are_you_taking_wa
                    ph = excluded.ph
                    temperature = excluded.temperature
                    conductivity = excluded.conductivity
                    total_dissolved = excluded.total_dissolved
                    dissolved_oxygen = excluded.dissolved_oxygen
                    other_comment = excluded.other_comment
        """

        execute_values(self._cursor, sql, points)

    def close(self):
        self._connection.commit()
        self._cursor.close()
        self._connection.close()
