import os

from epicollect_migrator.epicollect import Epicollect
from epicollect_migrator.database import Database


epicollect_v1 = Epicollect(
    base_url=os.environ['EPICOLLECT_BASE_URL'],
    project_name=os.environ['EPICOLLECT_PROJECT_NAME'],
    client_id=os.environ['EPICOLLECT_CLIENT_ID'],
    client_secret=os.environ['EPICOLLECT_CLIENT_SECRET'])

epicollect_v2 = Epicollect(
    base_url=os.environ['EPICOLLECT_BASE_URL'],
    project_name=os.environ['EPICOLLECT_PROJECT_NAME_2'],
    client_id=os.environ['EPICOLLECT_CLIENT_ID_2'],
    client_secret=os.environ['EPICOLLECT_CLIENT_SECRET_2'])


def handle(_, __):

    points_v1 = epicollect_v1.get_points(version_2=False)
    points_v2 = epicollect_v2.get_points(version_2=True)

    database = Database.connect(connection_uri=os.environ['DATABASE_CONNECTION_URI'])
    database.add_v1_points(points_v1)
    database.add_v2_points(points_v2)
    database.close()


if __name__ == '__main__':
    handle({}, {})
