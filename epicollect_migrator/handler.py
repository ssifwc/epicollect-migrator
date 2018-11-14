import os

from epicollect_migrator.epicollect import Epicollect
from epicollect_migrator.database import Database
from epicollect_migrator.image_store import ImageStore


epicollect = Epicollect(
    base_url=os.environ['EPICOLLECT_BASE_URL'],
    project_name=os.environ['EPICOLLECT_PROJECT_NAME'],
    client_id=os.environ['EPICOLLECT_CLIENT_ID'],
    client_secret=os.environ['EPICOLLECT_CLIENT_SECRET'])

image_store = ImageStore(epicollect, bucket_name=os.environ['BUCKET_NAME'])


def handle(_, __):

    points = epicollect.get_points()

    image_store.add_points(points)

    database = Database.connect(connection_uri=os.environ['DATABASE_CONNECTION_URI'])
    database.add_field_points(points)
    database.close()
