import requests
from shapely.geometry import Point
import json

from epicollect_migrator.wetted_width_flow import WettedWidthFlow


class EpicollectV2Parser:

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

        v2_json_2_v3 = EpicollectV2Parser._parse_point_v2(data)

        return [
            data.get('ec5_uuid'),
            EpicollectV2Parser.get_coordinates_as_point(v2_json_2_v3),
            EpicollectV2Parser.get_flow_rate(v2_json_2_v3),
            json.dumps(EpicollectV2Parser._parse_point_v2(data))
        ]

    @staticmethod
    def _parse_point_v2(data):
        """
        :type data: dict
        :rtype: dict
        """
        mapped = {'ec5_uuid': data.get('ec5_uuid'),
                  'created_at': data.get('created_at'),
                  'created_by': data.get('created_by'),
                  'title': data.get('title'),
                  'monitor_location': data.get('LocName'),
                  'other_location': EpicollectV2Parser.get_other_location(data),
                  'walker': data.get('2_I_am_a_hiker_walke'),
                  'hiker_name': data.get('3_Name_or_Initials'),
                  'hiker_date': data.get('4_Date'),
                  'hiker_time': data.get('6_Time'),
                  'photo_record': data.get('6_Photo'),
                  'water_body': data.get('WaterBodyType'),
                  'water_movement': data.get('8_Water_movement'),
                  'coordinates': data.get('Coor'),
                  'monitor_date': data.get('Date'),
                  'monitor_time': data.get('Time'),
                  'temperature': data.get('Temp'),
                  'cloud_cover': data.get('CloudCover'),
                  'last_sign_precip': data.get('LastSigPrecip'),
                  'safe_to_work': data.get('SafetoWork'),
                  'name': data.get('Name'),
                  'no_of_people': data.get('30__of_Participants'),
                  'gauge_depth_cm': data.get('28_Staff_Gauge_Depth'),
                  'water_moving': data.get('WaterMoving'),
                  'flow_type': data.get('FlowType'),
                  'visit_type': data.get('VisitType'),
                  'gen_land_use': data.get('GenLandUse'),
                  'other_land_use': data.get('OtherLandUse'),
                  'water_use': data.get('WaterUse'),
                  'other_water_use': data.get('OtherWaterUse'),
                  'drainage_sources': data.get('DrainageSources'),
                  'terrain': data.get('Terrain'),
                  'water_level': data.get('WaterLevel'),
                  'vegetation': data.get('Vegetation'),
                  'canopy_coverage': data.get('CanopyCoverage'),
                  'surficial_geology': data.get('SurficicalGeology'),
                  'water_surface': data.get('WaterSurface'),
                  'algae': data.get('Algae'),
                  'algae_extent': data.get('AlgaeExtent'),
                  'aquatic_life': data.get('AquaticLife'),
                  'other_species': data.get('OtherSpecies'),
                  'depth_wl': data.get('DepthWL'),
                  'location': data.get('Location'),
                  'reference': data.get('55_Describe_referenc'),
                  'photo_pond': data.get('56_Photo_of_water_le'),
                  'flow_measure_loc': data.get('FlowMeasureLoc'),
                  'wetted_width_cm': data.get('WettedWidth_cm'),
                  'water_color': data.get('WaterColor'),
                  'water_turbidity': data.get('58_Water_Turbidity_q'),
                  'qual_or_quant': data.get('TypeMeasure'),
                  'rate_of_flow': data.get('RateofFlow'),
                  'describe_water_level': data.get('DescribeWaterLevel'),
                  'culvert_diameter': data.get('CulvertDia'),
                  'wet_width_CMP_cm': data.get('WetWidthCulvertcm'),
                  'max_depth_water_cm': data.get('MaxDepthWatercm'),
                  'X_area_CMP_cm2': data.get('XsecAreaCulvert_c'),
                  'method_of_measure': data.get('MethodMeasure'),
                  'D1streamm': data.get('D1streamm'),
                  'W1P1': data.get('W1P1'),
                  'D1P1': data.get('D1P1'),
                  'W2P2': data.get('W2P2'),
                  'D2P2': data.get('D2P2'),
                  'W3P3': data.get('W3P3'),
                  'D3P3': data.get('D3P3'),
                  'W4P4': data.get('W4P4'),
                  'D4P4': data.get('D4P4'),
                  'W5P5': data.get('W5P5'),
                  'D5P5': data.get('D5P5'),
                  'W6P6': data.get('W6P6'),
                  'D6P6': data.get('D6P6'),
                  'W7D7': data.get('W7D7'),
                  'D7P7': data.get('D7P7'),
                  'W8D8': data.get('W8D8'),
                  'D8P8': data.get('D8P8'),
                  'W9P9': data.get('W9P9'),
                  'D9P9': data.get('D9P9'),
                  'W10P10': data.get('W10P10'),
                  'D10P10': data.get('D10P10'),
                  'BandTLpersec': data.get('BandTLpersec'),
                  'float_flow_lpersec': data.get('FlowRateLpersec'),
                  'T1s': data.get('T1s'),
                  'T2s': data.get('T2s'),
                  'T3s': data.get('T3s'),
                  'additional_photo_1': data.get('36_Additional_Photo_'),
                  'additional_photo_2': data.get('37_Additional_Photo_'),
                  'short_video': data.get('61_Short_video'),
                  'ph_oakton': data.get('phOakton'),
                  'temperature_water': data.get('TempWater'),
                  'conductivity': data.get('Cond'),
                  'total_dissolve_solid': data.get('122_Total_Dissolved_'),
                  'dissolved_oxygen': data.get('DO'),
                  'alkality': data.get('Alk'),
                  'hardness': data.get('Hard'),
                  'other_comments': data.get('36_Other_comments'),
                  'photo_wq1': data.get('125_Photo_Water_Qual'),
                  'photo_wq2': data.get('126_Photo_Water_Qual'),
                  'photo_us': data.get('35_Photos'),
                  'photo_ds': data.get('42_Photo__view_downs')

                 # '': data.get('66_Simple_or_detaile'),
                 # '': data.get('74_Quantitative_Meas'),


                  }

        return mapped

    @staticmethod
    def get_other_location(data):
        if data.get('SubLocNorth'):
            return data.get('SubLocNorth')
        elif data.get('SubLocCentral'):
            return data.get('SubLocCentral')
        elif data.get('SubLocSouth'):
            return data.get('SubLocSouth')
        elif data.get('OtherLocNorth'):
            return data.get('OtherLocNorth')
        elif data.get('OtherLocCent'):
            return data.get('OtherLocCent')
        elif data.get('OtherLocSouth'):
            return data.get('OtherLocSouth')

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
