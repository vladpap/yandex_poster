import os
from urllib.parse import urlparse

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from tqdm import tqdm

from ...models import Image, Point


def tqdm_enumerate(iter):
    i = 0
    for y in tqdm(iter):
        yield i, y
        i += 1


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(options['url_json_position'])
        response.raise_for_status()
        point_from_url = response.json()
        point, created = Point.objects.get_or_create(
            title=point_from_url['title'],
            description_short=point_from_url['description_short'],
            description_long=point_from_url['description_long'],
            longitude=point_from_url['coordinates']['lng'],
            latitude=point_from_url['coordinates']['lat']
            )

        for index, image_url in tqdm_enumerate(point_from_url['imgs']):
            response = requests.get(image_url)
            response.raise_for_status()

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(response.content)
            img_temp.flush()

            file_name = os.path.basename(urlparse(image_url).path)
            image = Image()
            image.image.save(file_name,
                             File(img_temp),
                             save=False)
            image.to_point = point
            image.position = index
            image.save()

    def add_arguments(self, parser):
        parser.add_argument('url_json_position',
                            type=str,
                            help='URL данных в json, информации о локации'
                            )
