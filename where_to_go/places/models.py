from django.db import models
from django.conf import settings



class Point(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название')

    description_short = models.CharField(
        verbose_name='Короткое описание',
        max_length=500,
        db_index=True)

    description_long = models.TextField(
        verbose_name='Описание')

    longitude = models.DecimalField(
        verbose_name='Долгота',
        max_digits=16,
        decimal_places=14)

    latitude = models.DecimalField(
        verbose_name='Широта',
        max_digits=16,
        decimal_places=14)

    class Meta:
        verbose_name = 'Места'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title

    def get_point_from_id(id):
        point = Point.objects.filter(id=id).first()
        images = []
        for image in point.images.all():
            images.append(f'.{image.image.url}')
        asd = {
            "title": point.title,
            "imgs": images,
            "description_short": point.description_short,
            "description_long": point.description_long,
            "coordinates": {
                "lng": point.longitude,
                "lat": point.latitude
                }
        }
        return asd


class Image(models.Model):
    image = models.ImageField(
        verbose_name='Фото')

    to_point = models.ForeignKey(
        Point,
        verbose_name='К локации',
        related_name='images',
        on_delete=models.CASCADE,
        null=False)

    position = models.IntegerField(
        verbose_name='Позиция',
        db_index=True,
        unique=True,
        null=False)

    class Meta:
        verbose_name = 'Фоторгафия'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{str(self.position)} {self.to_point.title}'
