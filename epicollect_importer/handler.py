import os
import time

from epicollect_importer.epicollect_parser import EpicollectParser
from epicollect_importer.epicollect_v2_parser import EpicollectV2Parser
from epicollect_importer.database import Database


def handle(_, __):
    epicollect_v2 = EpicollectV2Parser(
        base_url=os.environ['EPICOLLECT_BASE_URL'],
        project_name=os.environ['EPICOLLECT_PROJECT_NAME_2'])

    epicollect_v3 = EpicollectParser(
        base_url=os.environ['EPICOLLECT_BASE_URL'],
        project_name=os.environ['EPICOLLECT_PROJECT_NAME_3'])

    print('getting points from epicollect ... ')
    database = Database.connect(connection_uri=os.environ['DATABASE_CONNECTION_URI'])

    try:
        print('migrating V2 data')
        observations_v2 = epicollect_v2.get_field_observations()
        database.add_field_observations(observations_v2)
        print('Done migrating V2 data')
        time.sleep(60) # epicollect throttles when too many requests are done too quickly, let's hang out here a bit
    except:
        print('Aborting V2 migration, any exception just assumes it is turned off (no public access)')

    print('migrating V3 data')
    observations_v3 = epicollect_v3.get_field_observations()
    database.add_field_observations(observations_v3)
    print('Done migrating V3 data')

    database.close()
    print('committed field observations in db.')


if __name__ == '__main__':
    handle({}, {})


