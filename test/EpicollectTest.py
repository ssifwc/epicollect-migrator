import unittest

from epicollect_migrator_lambda.handler import handle
from test.support import EnvironmentVarGuard


class EpicollectTest(unittest.TestCase):

    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('EPICOLLECT_BASE_URL', 'https://five.epicollect.net')
        self.env.set('EPICOLLECT_PROJECT_NAME', 'SSI WATERSHED STEWARDSHIP GROUP')
        self.env.set('EPICOLLECT_PROJECT_NAME_2', 'SSI WATERSHED GROUPS VERSION 2')
        self.env.set('DATABASE_CONNECTION_URI', 'postgresql://postgres:password@localhost:5432/postgres')

    def test(self):
        handle()


if __name__ == '__main__':
    unittest.main()
