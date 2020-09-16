import unittest

from epicollect_importer.wetted_width_flow import WettedWidthFlow


class WettedWidthFlowTest(unittest.TestCase):

    def test_flow_without_datapoints(self):
        wetted_flow = WettedWidthFlow()
        self.assertIs(wetted_flow.calculate_flow_rate({}), None)
        self.assertIs(wetted_flow.calculate_flow_rate(get_test_values_and_remove('W1P1')), None)
        self.assertIs(wetted_flow.calculate_flow_rate(get_test_values_and_remove('D1P1')), None)
        self.assertIs(wetted_flow.calculate_flow_rate(get_test_values_and_remove('W2P2')), None)
        self.assertIs(wetted_flow.calculate_flow_rate(get_test_values_and_remove('D2P2')), None)
        self.assertIs(wetted_flow.calculate_flow_rate(get_test_values_and_remove('W3P3')), None)
        self.assertIs(wetted_flow.calculate_flow_rate(get_test_values_and_remove('D3P3')), None)
        self.assertIs(wetted_flow.calculate_flow_rate(get_test_values_and_remove('D1streamm')), None)

    def test_flow_calculation(self):
        self.assertEqual(WettedWidthFlow().calculate_flow_rate(get_test_values()), 26.36)


def get_test_values():
    return {'W1P1': 27.9, 'D1P1': 25.4, 'W2P2': 43.2, 'D2P2': 27.9, 'W3P3': 158.4,
            'D3P3': 27.9, 'T1s': 9.0, 'T2s': 11.0, 'T3s': 11.0, 'D1streamm': 2.74}


def get_test_values_and_remove(key):
    values = {'W1P1': 27.9, 'D1P1': 25.4, 'W2P2': 43.2, 'D2P2': 27.9, 'W3P3': 158.4,
              'D3P3': 27.9, 'T1s': 9.0, 'T2s': 11.0, 'T3s': 11.0, 'D1streamm': 2.74}
    values.pop(key)
    return values


if __name__ == '__main__':
    unittest.main()
