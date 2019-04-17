import requests
from shapely.geometry import Point


class Epicollect:

    def __init__(self, base_url, project_name, client_id, client_secret):

        self._base_url = base_url
        self._search_endpoint = f'{base_url}/api/export/entries/{project_name}'
        self._media_endpoint = f'{base_url}/api/export/media/{project_name}'
        self._client_id = client_id
        self._client_secret = client_secret

    def get_points(self, version_2=True):

        access_token = self._get_token()

        return self._get_data(self._search_endpoint, access_token, data=[], version_2=version_2)

    def get_image(self, image_id):

        url = f'{self._media_endpoint}?type=photo&format=entry_original&name={image_id}'

        response = requests.get(url, headers={'Authorization': 'Bearer ' + self._get_token()})

        return response

    def _get_data(self, url, access_token, data, version_2=True):

        response = self._get_response(url, access_token)
        new_data = self._get_data_from_response(response, version_2) + data

        if self._response_has_next(response):
            return self._get_data(response['links']['next'], access_token, new_data, version_2)

        return new_data

    def _get_token(self):
        params = {
            'grant_type': 'client_credentials',
            'client_id': self._client_id,
            'client_secret': self._client_secret
        }

        response = requests.post(f'{self._base_url}/api/oauth/token', data=params)

        return response.json()['access_token']

    @staticmethod
    def _response_has_next(response):
        """
        :type response: dict
        :rtype: bool
        """

        return bool(response['links']['next'])

    @staticmethod
    def _get_response(url, access_token):
        """
        :type url: str
        :type access_token: str
        :rtype: dict
        """

        response = requests.get(url, headers={'Authorization': 'Bearer ' + access_token})

        return response.json()

    def _get_data_from_response(self, response, version_2=True):
        """
        :type response: dict
        :rtype: list[list]
        """

        if version_2:
            parse_point = self._parse_point_v2
        else:
            parse_point = self._parse_point_v1

        points = []
        for point in response['data']['entries']:
                points.append(parse_point(point))
        return points

    @staticmethod
    def _parse_point_v1(data):
        """
        :type data: dict
        :rtype: list
        """

        location = data['6_Where_am_I']
        longitude, latitude = location['longitude'], location['latitude']
        if type(longitude) is str and type(latitude) is str:
            point = None
        else:
            point = Point(longitude, latitude).wkt

        number_of_participants = parse_int(data['13_No_of_Participant'])
        temperature = parse_float(data['51_Temperature'])
        conductivity = parse_float(data['52_Conductivity'])
        ph = parse_float(data['50_pH'])
        flow_rate_1 = parse_float(data['35_Flow_Rate_Quantit'])
        flow_rate_2 = parse_float(data['36_Flow_Rate_Quantit'])
        flow_rate_3 = parse_float(data['37_Flow_Rate_Quantit'])

        return [
            data['ec5_uuid'],
            data['created_at'],
            data['created_by'],
            data['title'],
            data['1_Location_Name_Desc'],
            'water_matters',
            data['2_General_Island_Are'],
            data['3_Named_Location_if_'],
            data['4_Watershed'],
            point,
            data['9_Weather_check_all_'],
            data['10_Last_Significant_'],
            data['11_Safe_to_work_at_t'],
            data['12_Name_initials_or_'],
            number_of_participants,
            data['14_Type_of_Visit'],
            data['15_General_Land_use_'],
            data['16_Describe_other_La'],
            data['17_Types_of_Water_Us'],
            data['18_Describe_Other_Wa'],
            data['19_This_area_receive'],
            data['20_Describe_other_dr'],
            data['21_Vegetation_in_Are'],
            data['22_Canopy_coverage_w'],
            data['23_SoilRock_Type'],
            data['24_Water_Body_Type'],
            data['25_Water_Body_Name_i'],
            data['26_Water_Movement_Vi'],
            data['27_Likely_permanance'],
            data['28_Flow_Measurement_'],
            data['29_Describe_other_fl'],
            data['30_Wetted_Width_m'],
            data['31_Rate_of_Flow_qual'],
            data['32_Describe_Water_Le'],
            data['33_Method_of_Measure'],
            data['34_Describe_Other_Me'],
            flow_rate_1,
            flow_rate_2,
            flow_rate_3,
            data['38_Any_of_the_follow'],
            data['39_Type_of_Algae_if_'],
            data['41_Evidence_of_Aquat'],
            data['42_Describe_other_in'],
            data['43_Water_color_hue'],
            data['44_Photo__view_upstr'],
            data['45_Photo__view_downs'],
            data['46_Do_you_want_to_ta'],
            data['47_Additional_Photo_'],
            data['48_Additional_Photo_'],
            data['49_Are_you_taking_wa'],
            ph,
            temperature,
            conductivity,
            data['53_Other_comments']
        ]

    @staticmethod
    def _parse_point_v2(data):
        """
        :type data: dict
        :rtype: list
        """

        location = data.get('Coor')
        longitude, latitude = location['longitude'], location['latitude']
        if type(longitude) is str or type(latitude) is str:
            point = None
        else:
            point = Point(longitude, latitude).wkt

        return [
            data.get('ec5_uuid'),
             data.get('created_at'),
             data.get('created_by'),
             data.get('title'),
             data.get('LocName'),
             data.get('2_I_am_a_hiker_walke'),
             data.get('4_Date'),
             data.get('6_Photo'),
             data.get('7_Water_Body_Type'),
             data.get('8_Water_movement'),
             data.get('7_Brief_Description'),
             data.get('8_Should_SSIFWC_visi'),
             data.get('IslandArea'),
             data.get('SubLocNorth'),
             data.get('SubLocCentral'),
             data.get('SubLocSouth'),
             data.get('OtherLocNorth'),
             data.get('OtherLocCent'),
             data.get('OtherLocSouth'),
             point,
             data.get('Date'),
             data.get('Time'),
             data.get('Temp'),
             data.get('CloudCover'),
             data.get('Precip'),
             data.get('LastSigPrecip'),
             data.get('SafetoWork'),
             data.get('Name'),
             data.get('30__of_Participants'),
             data.get('WaterMoving'),
             data.get('FlowType'),
             data.get('VisitType'),
             data.get('GenLandUse'),
             data.get('OtherLandUse'),
             data.get('WaterUse'),
             data.get('OtherWaterUse'),
             data.get('DrainageSources'),
             data.get('Terrain'),
             data.get('WaterLevel'),
             data.get('Vegetation'),
             data.get('CanopyCoverage'),
             data.get('SurficicalGeology'),
             data.get('WaterSurface'),
             data.get('Algae'),
             data.get('AlgaeExtent'),
             data.get('AquaticLife'),
             data.get('OtherSpecies'),
             data.get('56_Absolute_Depth_Me'),
             data.get('57_Describe_location'),
             data.get('55_Describe_referenc'),
             data.get('56_Photo_of_water_le'),
             data.get('FlowMeasure'),
             data.get('FlowMeasureLoc'),
             data.get('55_Current_Wetted_Wi'),
             data.get('56_Estimated_wetted_'),
             data.get('WaterColor'),
             data.get('58_Water_Turbidity_q'),
             data.get('TypeMeasure'),
             data.get('RateofFlow'),
             data.get('DescribeWaterLevel'),
             data.get('MethodMeasure'),
             data.get('66_Simple_or_detaile'),
             data.get('67_Measure_depth_cm_'),
             data.get('71_Distance_from_ban'),
             data.get('70_Depth_at_pt_1_cm'),
             data.get('73_Distance_from_ban'),
             data.get('72_Depth_at_pt_2_cm'),
             data.get('75_Distance_from_ban'),
             data.get('74_Depth_at_pt_3_cm'),
             data.get('77_Distance_from_ban'),
             data.get('76_Depth_at_pt_4_cm'),
             data.get('79_Distance_from_ban'),
             data.get('78_Depth_at_pt_5_cm'),
             data.get('81_Distance_from_ban'),
             data.get('80_Depth_at_pt_6_cm'),
             data.get('83_Distance_from_ban'),
             data.get('82_Depth_at_pt_7_cm'),
             data.get('85_Distance_from_ban'),
             data.get('84_Depth_of_pt_8_cm'),
             data.get('87_Distance_from_ban'),
             data.get('86_Depth_at_pt_9_cm'),
             data.get('88_Depth_at_pt_10_cm'),
             data.get('74_Quantitative_Meas'),
             data.get('60_Velocity_1_ms'),
             data.get('61_Velocity_2_ms'),
             data.get('62_Velocity_3_ms'),
             data.get('63_Depth_to_meter_fr'),
             data.get('64_Depth_from_meter_'),
             data.get('75_Enter_Xsection_Ar'),
             data.get('91_Distance_Traveled'),
             data.get('92_Time_1_sec'),
             data.get('93_Time_2_sec'),
             data.get('94_Time_3_sec'),
             data.get('81_Enter_XSection_Ar'),
             data.get('108_Flow_Rate_averag'),
             data.get('35_Measurement_1_Ls'),
             data.get('61_Measurement_1_Tim'),
             data.get('36_Measurement_2_Ls'),
             data.get('63_Measurement_2_Tim'),
             data.get('37_Measurement_3_Ls'),
             data.get('65_Measurement_3_Tim'),
             data.get('54_Are_you_taking_ph'),
             data.get('35_Photos'),
             data.get('42_Photo__view_downs'),
             data.get('35_Do_you_want_to_ta'),
             data.get('36_Additional_Photo_'),
             data.get('37_Additional_Photo_'),
             data.get('61_Short_video'),
             data.get('46_Are_you_taking_wa'),
             data.get('59_pH'),
             data.get('60_Temperature'),
             data.get('61_Conductivity'),
             data.get('122_Total_Dissolved_'),
             data.get('123_Dissolved_Oxygen'),
             data.get('36_Other_comments')
        ]


def parse_float(value):

    try:
        return float(value)
    except Exception:
        return None


def parse_int(value):

    try:
        return int(value)
    except Exception:
        return None
