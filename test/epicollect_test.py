import unittest

from epicollect_migrator.handler import handle
from test.support import EnvironmentVarGuard


class EpicollectTest(unittest.TestCase):

    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('EPICOLLECT_BASE_URL', 'https://five.epicollect.net')
        self.env.set('EPICOLLECT_PROJECT_NAME', 'ssi-watershed-stewardship-group')
        self.env.set('EPICOLLECT_PROJECT_NAME_2', 'ssi-watershed-groups-version-2')
        self.env.set('DATABASE_CONNECTION_URI', 'postgresql://postgres:password@localhost:5432/postgres')

    def test_epicollect(self):
        handle('how cares', 'still dont care')


if __name__ == '__main__':
    unittest.main()
