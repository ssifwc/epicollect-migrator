class WettedWidthFlow:
    measurement_fields = ['W1P1', 'D1P1', 'W2P2', 'D2P2', 'W3P3', 'D3P3', 'W4P4', 'D4P4', 'W5P5', 'D5P5', 'W6P6',
                          'D6P6', 'W7D7', 'D7P7', 'W8D8', 'D8P8', 'W9P9', 'D9P9', 'W10P10', 'D10P10', 'T1s', 'T2s',
                          'T3s', 'D1streamm']

    def calculate_flow_rate(self, data):

        if not self.is_data_valid(data):
            return None

        ts_dict = self.extract_time_value_to_dict(data)
        if len(ts_dict) < 1:
            return None

        print(' ')
        print('EPICOLLECT ID: ' + str(data.get('ec5_uuid')))

        xsecareacm2 = self.get_cross_section(data)

        d1streamm = parse_float(data.get('D1streamm'))
        average_t = sum(ts_dict.values()) / len(ts_dict)
        flow = 0.25 * (d1streamm / average_t) * (xsecareacm2 / 10)

        print('FLOW: 0.25 * (' + str(d1streamm) + '/' + str(average_t) + ' * ' + str(xsecareacm2) + ' / 10 = ' + str(
            round(flow, 2)))

        return round(flow, 2)

    def get_cross_section(self, data):
        W1P1 = parse_float(data.get('W1P1'))
        D1P1 = parse_float(data.get('D1P1'))
        W2P2 = parse_float(data.get('W2P2'))
        D2P2 = parse_float(data.get('D2P2'))
        W3P3 = parse_float(data.get('W3P3'))
        D3P3 = parse_float(data.get('D3P3'))
        W4P4 = parse_float(data.get('W4P4'))
        D4P4 = parse_float(data.get('D4P4'))
        W5P5 = parse_float(data.get('W5P5'))
        D5P5 = parse_float(data.get('D5P5'))
        W6P6 = parse_float(data.get('W6P6'))
        D6P6 = parse_float(data.get('D6P6'))
        W7D7 = parse_float(data.get('W7P7'))  # typo: should be W7P7 ... epicollect seems wrong
        D7P7 = parse_float(data.get('D7P7'))
        W8D8 = parse_float(data.get('W8D8'))
        D8P8 = parse_float(data.get('D8P8'))
        W9P9 = parse_float(data.get('W9P9'))
        D9P9 = parse_float(data.get('D9P9'))
        W10P10 = parse_float(data.get('W10P10'))
        D10P10 = parse_float(data.get('D10P10'))

        equation = '(' + str(W1P1) + ' - 0) * 0.5 * ' + str(D1P1) + ' + (' + str(W2P2) + ' - ' + str(W1P1) + \
                   ') * 0.5 * (' + str(D2P2) + ' + ' + str(D1P1) + ') + (' + str(W3P3) + ' - ' + str(W2P2) + \
                   ') * 0.5 * (' + str(D3P3) + ' + ' + str(D2P2) + ')'
        xsecareacm2 = (W1P1 - 0) * 0.5 * D1P1
        xsecareacm2 = xsecareacm2 + (W2P2 - W1P1) * 0.5 * (D2P2 + D1P1)
        xsecareacm2 = xsecareacm2 + (W3P3 - W2P2) * 0.5 * (D3P3 + D2P2)

        if W4P4 is not None and D4P4 is not None:
            equation = equation + ' + (' + str(W4P4) + ' - ' + str(W3P3) + ') * 0.5 * (' + str(D4P4) + ' + ' + str(
                D3P3) + ')'
            xsecareacm2 = xsecareacm2 + (W4P4 - W3P3) * 0.5 * (D4P4 + D3P3)
        if W5P5 is not None and D5P5 is not None:
            equation = equation + ' + (' + str(W5P5) + ' - ' + str(W4P4) + ') * 0.5 * (' + str(D5P5) + ' + ' + str(
                D4P4) + ')'
            xsecareacm2 = xsecareacm2 + (W5P5 - W4P4) * 0.5 * (D5P5 + D4P4)
        if W6P6 is not None and D6P6 is not None:
            equation = equation + ' + (' + str(W6P6) + ' - ' + str(W5P5) + ') * 0.5 * (' + str(D6P6) + ' + ' + str(
                D5P5) + ')'
            xsecareacm2 = xsecareacm2 + (W6P6 - W5P5) * 0.5 * (D6P6 + D5P5)
        if W7D7 is not None and D7P7 is not None:
            equation = equation + ' + (' + str(W7D7) + ' - ' + str(W6P6) + ') * 0.5 * (' + str(D7P7) + ' + ' + str(
                D6P6) + ')'
            xsecareacm2 = xsecareacm2 + (W7D7 - W6P6) * 0.5 * (D7P7 + D6P6)
        if W8D8 is not None and D8P8 is not None:
            equation = equation + ' + (' + str(W8D8) + ' - ' + str(W7D7) + ') * 0.5 * (' + str(D8P8) + ' + ' + str(
                D7P7) + ')'
            xsecareacm2 = xsecareacm2 + (W8D8 - W7D7) * 0.5 * (D8P8 + D7P7)
        if W9P9 is not None and D9P9 is not None:
            equation = equation + ' + (' + str(W9P9) + ' - ' + str(W8D8) + ') * 0.5 * (' + str(D9P9) + ' + ' + str(
                D8P8) + ')'
            xsecareacm2 = xsecareacm2 + (W9P9 - W8D8) * 0.5 * (D9P9 + D8P8)
        if W10P10 is not None and D10P10 is not None:
            equation = equation + ' + (' + str(W10P10) + ' - ' + str(W9P9) + ') * 0.5 * (' + str(D10P10) + ' + ' + str(
                W10P10) + ')'
            xsecareacm2 = xsecareacm2 + (W10P10 - W9P9) * 0.5 * (D10P10 + W10P10)

        return xsecareacm2

    @staticmethod
    def extract_time_value_to_dict(data):
        ts_dict = {}
        if data.get('T1s'):
            ts_dict['T1s'] = parse_float(data.get('T1s'))
        if data.get('T2s'):
            ts_dict['T2s'] = parse_float(data.get('T2s'))
        if data.get('T3s'):
            ts_dict['T3s'] = parse_float(data.get('T3s'))
        return ts_dict

    @staticmethod
    def is_data_valid(data):
        if not data.get('W1P1') \
                or data.get('D1P1') is None \
                or data.get('W2P2') is None \
                or data.get('D2P2') is None \
                or data.get('W3P3') is None \
                or data.get('D3P3') is None \
                or data.get('D1streamm') is None:
            return False
        return True

    @staticmethod
    def get_wetted_width_flow_values(data):
        collected_values = ''
        for key in WettedWidthFlow.measurement_fields:
            if data.get(key) is not None:
                collected_values = collected_values + str(key)
                collected_values = collected_values + '=' + str(data.get(key)) + ', '
        return collected_values


def parse_float(value):
    try:
        return float(value)
    except Exception:
        return None
