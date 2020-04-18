import os

from epicollect_migrator_lambda.epicollect import Epicollect
from epicollect_migrator_lambda.database import Database


def handle():

    epicollect_v1 = Epicollect(
        base_url=os.environ['EPICOLLECT_BASE_URL'],
        project_name=os.environ['EPICOLLECT_PROJECT_NAME'])

    epicollect_v2 = Epicollect(
        base_url=os.environ['EPICOLLECT_BASE_URL'],
        project_name=os.environ['EPICOLLECT_PROJECT_NAME_2'])

    print('getting points from epicollect ... ')
    points_v1 = epicollect_v1.get_points(version_2=False)
    points_v2 = epicollect_v2.get_points(version_2=True)
    print('getting points done.')

    print('savings points in db ... ')
    database = Database.connect(connection_uri=os.environ['DATABASE_CONNECTION_URI'])
    database.add_v1_points(points_v1)
    database.add_v2_points(points_v2)
    database.close()
    print('savings points in db done.')


if __name__ == '__main__':
    handle({}, {})
