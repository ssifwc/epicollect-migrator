import requests
from shapely.geometry import Point
import json

from epicollect_importer.wetted_width_flow import WettedWidthFlow


class EpicollectParser:

    def __init__(self, base_url, project_name):
        self._base_url = base_url
        self._search_endpoint = f'{base_url}/api/export/entries/{project_name}'
        self._media_endpoint = f'{base_url}/api/export/media/{project_name}'

    def get_field_observations(self):
        return self._get_data(self._search_endpoint, data=[])

    def _get_data(self, url, data):
        response = self._get_response(url)
        new_data = self._get_data_from_response(response) + data

        if self._response_has_next(response):
            return self._get_data(response['links']['next'], new_data)

        return new_data

    def _get_data_from_response(self, response):
        """
        :type response: dict
        :rtype: list[list]
        """
        observations_json = []
        for observation in response['data']['entries']:
            observations_json.append(self._parse_point(observation, observation))
        return observations_json

    @staticmethod
    def _response_has_next(response):
        """
        :type response: dict
        :rtype: bool
        """
        return bool(response['links']['next'])

    @staticmethod
    def _get_response(url):
        """
        :type url: str
        :rtype: dict
        """
        return requests.get(url).json()

    @staticmethod
    def _parse_point(data, record):
        """
        :type data: dict
        :rtype: list
        """
        return [
            data.get('ec5_uuid'),
            EpicollectParser.get_coordinates_as_point(data),
            EpicollectParser.get_flow_rate(data),
            json.dumps(record)
        ]

    @staticmethod
    def get_coordinates_as_point(data):
        location = data.get('coordinates')
        longitude, latitude = location['longitude'], location['latitude']
        if type(longitude) is str or type(latitude) is str:
            point = None
        else:
            point = Point(longitude, latitude).wkt
        return point

    @staticmethod
    def get_flow_rate(data):
        try:
            wetted_width_flow = WettedWidthFlow().calculate_flow_rate(data)
        except:
            wetted_width_flow = None
        vessel_flow = data.get('BandTLpersec')
        meter_column_flow = data.get('FlowRateLpersec')
        if vessel_flow:
            flow_rate = vessel_flow
        elif wetted_width_flow:
            flow_rate = wetted_width_flow
        elif meter_column_flow:
            flow_rate = meter_column_flow
        else:
            flow_rate = None
        return flow_rate


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
