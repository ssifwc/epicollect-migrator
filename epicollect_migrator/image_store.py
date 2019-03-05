import boto3
from botocore.exceptions import ClientError


class ImageStore:

    def __init__(self, epicollect, bucket_name):

        self._epicollect = epicollect
        self._bucket_name = bucket_name
        self._s3 = boto3.resource('s3')

    def add_points(self, points, version='v1'):

        if version == 'v1':
            photo_indices = [44, 45, 47, 48]
        else:
            photo_indices = [102, 103, 105, 106]

        for point in points:
            for index in photo_indices:

                image_id = point[index]

                if image_id:

                    if not self._does_image_exist(image_id):
                        image = self._epicollect.get_image(image_id)
                        self._upload_image(image_id, image.content)

    def _upload_image(self, name, image):

        self._s3.Object(self._bucket_name, name).put(Body=image)

    def _does_image_exist(self, name):

        try:
            self._s3.Object(self._bucket_name, name).load()
            return True
        except ClientError:
            return False
