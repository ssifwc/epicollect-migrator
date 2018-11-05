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

    def add_field_points(self, points):

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

    def close(self):
        self._connection.commit()
        self._cursor.close()
        self._connection.close()
