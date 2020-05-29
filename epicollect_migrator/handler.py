import os

from epicollect_migrator.epicollect import Epicollect
from epicollect_migrator.database import Database


def handle(_, __):

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

    print('vessel_flow_count: ' + str(Epicollect.vessel_flow_count))
    print('wetted_width_count: ' + str(Epicollect.wetted_width_count))
    print('metric_column_count: ' + str(Epicollect.metric_column_count))


if __name__ == '__main__':
    handle({}, {})
