import unittest
import os

import psycopg2
from psycopg2.extras import RealDictCursor
from epicollect_migrator.database import Database
from epicollect_migrator.epicollect import Epicollect
from epicollect_migrator.handler import handle
from test.support import EnvironmentVarGuard


class EpicollectTest(unittest.TestCase):

    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('EPICOLLECT_BASE_URL', 'https://five.epicollect.net')
        self.env.set('EPICOLLECT_PROJECT_NAME', 'ssi-watershed-stewardship-group')
        self.env.set('EPICOLLECT_PROJECT_NAME_2', 'ssi-watershed-groups-version-2')
        self.env.set('DATABASE_CONNECTION_URI', 'postgresql://postgres:password@localhost:5432/postgres')

    def test_epicollect_migration_integration(self):
        handle('how cares', 'still dont care')

    def test_save_one_record(self):
        test_dict = self.get_test_record()
        record = {"data": {"entries": [test_dict]}}

        epicollect_v2 = Epicollect(
            base_url=os.environ['EPICOLLECT_BASE_URL'],
            project_name=os.environ['EPICOLLECT_PROJECT_NAME_2'])

        data = epicollect_v2._get_data_from_response(record, True)

        database = Database.connect(connection_uri=os.environ['DATABASE_CONNECTION_URI'])
        database.add_v2_points(data)
        database.close()

        connection = psycopg2.connect(os.environ['DATABASE_CONNECTION_URI'])
        cur = connection.cursor(cursor_factory=RealDictCursor)
        cur.execute(""" SELECT * from epicollect_observations_v2 """)

        result_json = cur.fetchall()
        first_row = result_json[0]

        self.assertEqual(test_dict.get('ec5_uuid'), first_row.get('uuid'))
        self.assertEqual(test_dict.get('created_at'), first_row.get('created_at'))
        self.assertEqual(test_dict.get('title'), first_row.get('title'))
        self.assertEqual(test_dict.get('LocName'), first_row.get('locname'))
        self.assertEqual(test_dict.get('Walker'), first_row.get('i_am_a_hiker_walker'))
        self.assertEqual(test_dict.get('DateW'), first_row.get('date'))
        self.assertEqual(test_dict.get('PhotoRec'), first_row.get('photo'))
        self.assertEqual(test_dict.get('WaterBody'), first_row.get('water_body_type'))
        self.assertEqual(test_dict.get('WaterMovement'), first_row.get('water_movement'))
        self.assertEqual(test_dict.get('IslandArea'), first_row.get('island_area'))
        self.assertEqual(test_dict.get('SubLocNorth'), first_row.get('sub_loc_north'))
        self.assertEqual(test_dict.get('SubLocCentral'), first_row.get('sub_loc_central'))
        self.assertEqual(test_dict.get('SubLocSouth'), first_row.get('sub_loc_south'))
        self.assertEqual(test_dict.get('OtherLocNorth'), first_row.get('other_loc_north'))
        self.assertEqual(test_dict.get('OtherLocCent'), first_row.get('other_loc_central'))
        self.assertEqual(test_dict.get('OtherLocSouth'), first_row.get('other_loc_south'))
        #self.assertEqual(test_dict.get('Coor'), first_row.get('Coor'))
        self.assertEqual(test_dict.get('Date'), first_row.get('date_2'))
        self.assertEqual(test_dict.get('Time'), first_row.get('time_2'))
        self.assertEqual(test_dict.get('Temp'), first_row.get('temp'))
        self.assertEqual(test_dict.get('CloudCover'), first_row.get('cloud_cover'))
        self.assertEqual(test_dict.get('LastSigPrecip'), first_row.get('last_sig_precipitation'))
        self.assertEqual(test_dict.get('SafetoWork'), first_row.get('safe_to_work'))
        self.assertEqual(test_dict.get('Name'), first_row.get('name'))
        self.assertEqual(test_dict.get('Peeps'), first_row.get('number_of_participants'))
        self.assertEqual(test_dict.get('WaterMoving'), first_row.get('water_moving'))
        self.assertEqual(test_dict.get('FlowType')[0],
                         first_row.get('flow_type').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('VisitType'), first_row.get('visit_type'))
        self.assertEqual(test_dict.get('GenLandUse')[0],
                         first_row.get('gen_land_use').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('OtherLandUse'),
                         first_row.get('other_land_use'))
        self.assertEqual(test_dict.get('WaterUse')[0],
                         first_row.get('water_use').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('OtherWaterUse'), first_row.get('other_water_use'))
        self.assertEqual(test_dict.get('DrainageSources')[0],
                         first_row.get('drainage_sources').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('Terrain'), first_row.get('terrain'))
        self.assertEqual(test_dict.get('WaterLevel'), first_row.get('water_level'))
        self.assertEqual(test_dict.get('Vegetation')[0],
                         first_row.get('vegetation').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('CanopyCoverage')[0],
                         first_row.get('canopy_coverage').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('SurficicalGeology')[0],
                         first_row.get('surficial_geology').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('WaterSurface')[0],
                         first_row.get('water_surface').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('Algae'), first_row.get('algae'))
        self.assertEqual(test_dict.get('AlgaeExtent'), first_row.get('algae_extent'))
        self.assertEqual(test_dict.get('AquaticLife')[0],
                         first_row.get('aquatic_life').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('OtherSpecies'), first_row.get('other_species'))
        self.assertEqual(test_dict.get('DepthWL'), first_row.get('absolute_depth_me'))
        self.assertEqual(test_dict.get('Location'), first_row.get('describe_location'))
        self.assertEqual(test_dict.get('Reference'), first_row.get('describe_reference'))
        self.assertEqual(test_dict.get('photo_of_water_le'), first_row.get('PhotoPond'))
        self.assertEqual(test_dict.get('FlowMeasureLoc')[0],
                         first_row.get('flow_measure_loc').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('WettedWidth'), first_row.get('current_wetted_wi'))
        self.assertEqual(test_dict.get('Esttwetwidth'), first_row.get('estimated_wetted'))
        self.assertEqual(test_dict.get('WaterColor')[0],
                         first_row.get('water_color').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('TypeMeasure'), first_row.get('type_measure'))
        self.assertEqual(test_dict.get('RateofFlow'), first_row.get('rate_of_flow'))
        self.assertEqual(test_dict.get('DescribeWaterLevel')[0],
                         first_row.get('describe_water_level').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('MethodMeasure')[0],
                         first_row.get('method_measure').replace('{', '').replace('}', ''))
        self.assertEqual(test_dict.get('66_Simple_or_detaile'), first_row.get('simple_or_detailed'))
        self.assertEqual(test_dict.get('MaxDepth'), first_row.get('measure_depth_cm'))
        self.assertEqual(test_dict.get('W1P1'), first_row.get('distance_from_ban_1'))
        self.assertEqual(test_dict.get('D1P1'), first_row.get('depth_at_pt_1_cm'))
        self.assertEqual(test_dict.get('W2P2'), first_row.get('distance_from_ban_2'))
        self.assertEqual(test_dict.get('D2P2'), first_row.get('depth_at_pt_2_cm'))
        self.assertEqual(test_dict.get('W3P3'), first_row.get('distance_from_ban_3'))
        self.assertEqual(test_dict.get('D3P3'), first_row.get('depth_at_pt_3_cm'))
        self.assertEqual(test_dict.get('W4P4'), first_row.get('distance_from_ban_4'))
        self.assertEqual(test_dict.get('D4P4'), first_row.get('depth_at_pt_4_cm'))
        self.assertEqual(test_dict.get('W5P5'), first_row.get('distance_from_ban_5'))
        self.assertEqual(test_dict.get('D5P5'), first_row.get('depth_at_pt_5_cm'))
        self.assertEqual(test_dict.get('W6P6'), first_row.get('distance_from_ban_6'))
        self.assertEqual(test_dict.get('D6P6'), first_row.get('depth_at_pt_6_cm'))
        self.assertEqual(test_dict.get('W7D7'), first_row.get('distance_from_ban_7'))
        self.assertEqual(test_dict.get('D7P7'), first_row.get('depth_at_pt_7_cm'))
        self.assertEqual(test_dict.get('W8D8'), first_row.get('distance_from_ban_8'))
        self.assertEqual(test_dict.get('D8P8'), first_row.get('depth_at_pt_8_cm'))
        self.assertEqual(test_dict.get('W9P9'), first_row.get('distance_from_ban_9'))
        self.assertEqual(test_dict.get('D9P9'), first_row.get('depth_at_pt_9_cm'))
        self.assertEqual(test_dict.get('W10P10'), first_row.get('distance_from_ban_10'))
        self.assertEqual(test_dict.get('D10P10'), first_row.get('depth_at_pt_10_cm'))
        self.assertEqual(test_dict.get('74_Quantitative_Meas'), first_row.get('quantitative_meas'))
        self.assertEqual(test_dict.get('V1msec'), first_row.get('velocity_1_ms'))
        self.assertEqual(test_dict.get('V2msec'), first_row.get('velocity_2_ms'))
        self.assertEqual(test_dict.get('V3msec'), first_row.get('velocity_3_ms'))
        self.assertEqual(test_dict.get('T1s'), first_row.get('time_1_sec'))
        self.assertEqual(test_dict.get('T2s'), first_row.get('time_2_sec'))
        self.assertEqual(test_dict.get('T3s'), first_row.get('time_3_sec'))
        self.assertEqual(test_dict.get('Vol1L'), first_row.get('measurement_1_ls'))
        self.assertEqual(test_dict.get('T1sBT'), first_row.get('measurement_1_tim'))
        self.assertEqual(test_dict.get('Vol2L'), first_row.get('measurement_2_ls'))
        self.assertEqual(test_dict.get('T2sBT'), first_row.get('measurement_2_tim'))
        self.assertEqual(test_dict.get('Vol3L'), first_row.get('measurement_3_ls'))
        self.assertEqual(test_dict.get('T3sBT'), first_row.get('measurement_3_tim'))
        self.assertEqual(test_dict.get('35_Photos'), first_row.get('photos'))
        self.assertEqual(test_dict.get('42_Photo__view_downs'), first_row.get('photo_view_downst'))
        self.assertEqual(test_dict.get('36_Additional_Photo_'), first_row.get('additional_photo_1'))
        self.assertEqual(test_dict.get('37_Additional_Photo_'), first_row.get('additional_photo_2'))
        self.assertEqual(test_dict.get('61_Short_video'), first_row.get('short_video'))
        self.assertEqual(test_dict.get('58_Water_Turbidity_q'), first_row.get('water_turbitidy_q'))
        self.assertEqual(test_dict.get('phOakton'), first_row.get('ph'))
        self.assertEqual(test_dict.get('TempWater'), first_row.get('temperature'))
        self.assertEqual(test_dict.get('Cond'), first_row.get('conductivity'))
        self.assertEqual(test_dict.get('TDS'), first_row.get('total_dissolved'))
        self.assertEqual(test_dict.get('DO'), first_row.get('dissolved_oxygen'))
        self.assertEqual(test_dict.get('Alk'), first_row.get('alkalinity'))
        self.assertEqual(test_dict.get('Hard'), first_row.get('hardness'))
        self.assertEqual(test_dict.get('36_Other_comments'), first_row.get('other_comments'))
        # TO BE ADDED
        #self.assertEqual(test_dict.get('W10P10'), first_row.get('distance_from_ban_10'))
        #self.assertEqual(test_dict.get('WaterBodyType'), first_row.get('WaterBodyType'))
        #self.assertEqual(test_dict.get('uploaded_at'), first_row.get('uploaded_at'))
        #self.assertEqual(test_dict.get('pHTestStrip'), first_row.get('pHTestStrip'))
        #self.assertEqual(test_dict.get('135_Chlorine_test_st'), first_row.get('135_Chlorine_test_st'))
        #self.assertEqual(test_dict.get('136_Air_Temperature'), first_row.get('136_Air_Temperature'))
        #self.assertEqual(test_dict.get('125_Photo_Water_Qual'), first_row.get('125_Photo_Water_Qual'))
        #self.assertEqual(test_dict.get('126_Photo_Water_Qual'), first_row.get('126_Photo_Water_Qual'))
        #self.assertEqual(test_dict.get('126_Oakton_Identific'), first_row.get('126_Oakton_Identific'))
        #self.assertEqual(test_dict.get('125_Weeks_since_last'), first_row.get('125_Weeks_since_last'))



    def get_test_record(self):
        return {"ec5_uuid": "c03f9c61-4189-4023-b36f-be1d8548d350",
                "created_at": "2020-07-02T17:04:53.613Z",
                "uploaded_at": "2020-07-02T17:05:54.000Z",
                "title": "title",
                "LocName": "LocName",
                "Walker": "Walker",
                "DateW": "12/12/2019",
                "PhotoRec": "PhotoRec",
                "WaterBody": "WaterBody",
                "WaterMovement": "WaterMovement",
                "CoordinatesH": "CoordinatesH",
                "IslandArea": "IslandArea",
                "SubLocNorth": "SubLocNorth",
                "SubLocCentral": "SubLocCentral",
                "SubLocSouth": "SubLocSouth",
                "OtherLocNorth": "OtherLocNorth",
                "OtherLocCent": "OtherLocCent",
                "OtherLocSouth": "OtherLocSouth",
                "Coor": {"latitude": 48.777713,
                         "longitude": -123.479909,
                         "accuracy": 10,
                         "UTM_Northing": 5402856,
                         "UTM_Easting": 464742,
                         "UTM_Zone": "10U"},
                "Date": "02/07/2020",
                "Time": "10:02:00",
                "Temp": "11 to 20 C",
                "CloudCover": "CouldCover",
                "LastSigPrecip": "LastSigPrecip",
                "SafetoWork": "SafetoWork",
                "Name": "Name",
                "Peeps": "Peeps",
                "WaterBodyType": "WaterBodyType",
                "WaterMoving": "WaterMoving",
                "FlowType": ["FlowType"],
                "VisitType": "VisitType",
                "GenLandUse": ["GenLandUse"],
                "OtherLandUse": "OtherLandUse",
                "WaterUse": ["WaterUse"],
                "OtherWaterUse": "OtherWaterUse",
                "DrainageSources": ["DrainageSources"],
                "Terrain": "Terrain",
                "WaterLevel": "WaterLevel",
                "Vegetation": ["Vegetation"],
                "CanopyCoverage": ["CanopyCoverage"],
                "SurficicalGeology": ["SurficicalGeology"],
                "WaterSurface": ["WaterSurface"],
                "Algae": "Algae",
                "AlgaeExtent": "AlgaeExtent",
                "AquaticLife": ["AquaticLife"],
                "OtherSpecies": "OtherSpecies",
                "DepthWL": "DepthWL",
                "Location": "Location",
                "Reference": "Reference",
                "PhotoPond": "PhotoPond",
                "FlowMeasureLoc": ["FlowMeasureLoc"],
                "WettedWidth": "WettedWidth",
                "Esttwetwidth": "Esttwetwidth",
                "WaterColor": ["WaterColor"],
                "TypeMeasure": "TypeMeasure",
                "RateofFlow": "RateofFlow",
                "DescribeWaterLevel": ["DescribeWaterLevel"],
                "MethodMeasure": ["MethodMeasure"],
                "66_Simple_or_detaile": "66_Simple_or_detaile",
                "MaxDepth": "MaxDepth",
                "W1P1": "W1P1",
                "D1P1": "D1P1",
                "W2P2": "W2P2",
                "D2P2": "D2P2",
                "W3P3": "W3P3",
                "D3P3": "D3P3",
                "W4P4": "W4P4",
                "D4P4": "D4P4",
                "W5P5": "W5P5",
                "D5P5": "D5P5",
                "W6P6": "W6P6",
                "D6P6": "D6P6",
                "W7D7": "W7D7",
                "D7P7": "D7P7",
                "W8D8": "W8D8",
                "D8P8": "D8P8",
                "W9P9": "W9P9",
                "D9P9": "D9P9",
                "W10P10": "W10P10",
                "D10P10": "D10P10",
                "74_Quantitative_Meas": "74_Quantitative_Meas",
                "FlowRateLpersec": "FlowRateLpersec",
                "V1msec": "V1msec",
                "V2msec": "V2msec",
                "V3msec": "V3msec",
                "Dtometer": "Dtometer",
                "DmetertoBot": "DmetertoBot",
                "XSecAreacm2": "XSecAreacm2",
                "FlowRateLpersecFloat": "FlowRateLpersecFloat",
                "D1streamm": "D1streamm",
                "T1s": "T1s",
                "T2s": "T2s",
                "T3s": "T3s",
                "Xsecareafloatcm2": "Xsecareafloatcm2",
                "BandTLpersec": "BandTLpersec",
                "Vol1L": "Vol1L",
                "T1sBT": "T1sBT",
                "Vol2L": "Vol2L",
                "T2sBT": "T2sBT",
                "Vol3L": "Vol3L",
                "T3sBT": "T3sBT",
                "35_Photos": "35_Photos",
                "42_Photo__view_downs": "42_Photo__view_downs",
                "36_Additional_Photo_": "36_Additional_Photo_",
                "37_Additional_Photo_": "37_Additional_Photo_",
                "61_Short_video": "61_Short_video",
                "58_Water_Turbidity_q": "58_Water_Turbidity_q",
                "125_Photo_Water_Qual": "https://five.epicollect.net/api/blah.jpg",
                "126_Photo_Water_Qual": "126_Photo_Water_Qual",
                "126_Oakton_Identific": "126_Oakton_Identific",
                "125_Weeks_since_last": "125_Weeks_since_last",
                "phOakton": "phOakton",
                "pHTestStrip": "pHTestStrip",
                "TempWater": "TempWater",
                "Cond": "Cond",
                "TDS": "TDS",
                "DO": "DO",
                "Alk": "Alk",
                "Hard": "Hard",
                "135_Chlorine_test_st": "135_Chlorine_test_st",
                "136_Air_Temperature": "136_Air_Temperature",
                "36_Other_comments": "36_Other_comments"}


if __name__ == '__main__':
    unittest.main()
