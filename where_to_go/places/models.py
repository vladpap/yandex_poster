from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Point(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название')

    short_description = models.TextField(
        verbose_name='Короткое описание',
        blank=True,
        null=True,
        db_index=True)

    long_description = HTMLField(
        verbose_name='Описание',
        blank=True,
        null=True)

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


class Image(models.Model):
    image = models.ImageField(
        verbose_name='Фото')

    to_point = models.ForeignKey(
        Point,
        verbose_name='К локации',
        related_name='images',
        on_delete=models.CASCADE)

    position = models.IntegerField(
        verbose_name='Позиция',
        db_index=True,
        blank=True,
        null=True,
        default=0)

    class Meta:
        verbose_name = 'Фоторгафия'
        verbose_name_plural = 'Фотографии'
        ordering = ['to_point__title']

    def __str__(self):
        return f'{str(self.position)} {self.to_point.title}'

    def get_thumbnail(self):
        return format_html(
            '<img src="{}" style='
            '"max-height:200px;max-width:300px;height:auto;width:auto;" />',
            self.image.url
        )

    def get_to_point(self):
        return self.to_point.title
