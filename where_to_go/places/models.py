from django.db import models


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
