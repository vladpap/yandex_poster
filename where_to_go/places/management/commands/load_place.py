import os
import urllib

import requests
from django.core.files import File
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
            short_description=point_from_url['description_short'],
            long_description=point_from_url['description_long'],
            longitude=point_from_url['coordinates']['lng'],
            latitude=point_from_url['coordinates']['lat']
            )

        for index, image_url in tqdm_enumerate(point_from_url['imgs']):
            image = Image()
            image.to_point = point
            image.position = index
            image.image.save(
                os.path.basename(image_url),
                File(open(urllib.request.urlretrieve(image_url)[0],
                          mode='rb')
                     )
                )

    def add_arguments(self, parser):
        parser.add_argument('url_json_position',
                            type=str,
                            help='URL данных в json, информации о локации'
                            )
