import os

from epicollect_migrator.epicollect import Epicollect
from epicollect_migrator.database import Database


def handle(_, __):

    epicollect_v2 = Epicollect(
        base_url=os.environ['EPICOLLECT_BASE_URL'],
        project_name=os.environ['EPICOLLECT_PROJECT_NAME_2'])

    print('getting points from epicollect ... ')
    points_v2 = epicollect_v2.get_points()
    print('getting points done.')

    print('savings points in db ... ')
    database = Database.connect(connection_uri=os.environ['DATABASE_CONNECTION_URI'])
    database.add_v2_points(points_v2)
    database.close()
    print('savings points in db done.')


if __name__ == '__main__':
    handle({}, {})
