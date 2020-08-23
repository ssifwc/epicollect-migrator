import requests
from shapely.geometry import Point

from epicollect_migrator.wetted_width_flow import WettedWidthFlow


class Epicollect:

    wetted_width_count = 0
    vessel_flow_count = 0
    metric_column_count = 0

    def __init__(self, base_url, project_name):
        self._base_url = base_url
        self._search_endpoint = f'{base_url}/api/export/entries/{project_name}'
        self._media_endpoint = f'{base_url}/api/export/media/{project_name}'

    def get_points(self):
        return self._get_data(self._search_endpoint, data=[])

    def _get_data(self, url, data):

        response = self._get_response(url)
        new_data = self._get_data_from_response(response) + data

        if self._response_has_next(response):
            return self._get_data(response['links']['next'], new_data)

        return new_data

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

        response = requests.get(url)

        return response.json()

    def _get_data_from_response(self, response):
        """
        :type response: dict
        :rtype: list[list]
        """
        parse_point = self._parse_point_v2
        points = []
        for point in response['data']['entries']:
            points.append(parse_point(point))
        return points


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
            Epicollect.get_flow_rate(data),
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
            data.get('phOakton'),
            data.get('TempWater'),
            data.get('Cond'),
            data.get('122_Total_Dissolved_'),
            data.get('DO'),
            data.get('Alk'),
            data.get('Hard'),
            data.get('36_Other_comments')
        ]

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
            Epicollect.vessel_flow_count = Epicollect.vessel_flow_count + 1
        elif wetted_width_flow:
            flow_rate = wetted_width_flow
            Epicollect.wetted_width_count = Epicollect.wetted_width_count + 1
        elif meter_column_flow:
            flow_rate = meter_column_flow
            Epicollect.metric_column_count = Epicollect.metric_column_count + 1
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
