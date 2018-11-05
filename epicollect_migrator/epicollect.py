import requests
from dateutil import parser
from shapely.geometry import Point


class Epicollect:

    def __init__(self, base_url, project_name, client_id, client_secret):

        self._base_url = base_url
        self._search_endpoint = f'{base_url}/api/export/entries/{project_name}'
        self._client_id = client_id
        self._client_secret = client_secret

    def get_points(self):

        access_token = self._get_token()

        return self._get_data(self._search_endpoint, access_token, data=[])

    def _get_data(self, url, access_token, data):

        response = self._get_response(url, access_token)
        new_data = self._get_data_from_response(response) + data

        if self._response_has_next(response):
            return self._get_data(response['links']['next'], access_token, new_data)

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

    def _get_data_from_response(self, response):
        """
        :type response: dict
        :rtype: list[list]
        """

        return [self._parse_point(point) for point in response['data']['entries']]

    @staticmethod
    def _parse_point(data):
        """
        :type data: list
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
