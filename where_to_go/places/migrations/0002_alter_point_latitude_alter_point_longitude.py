# Generated by Django 4.2.4 on 2023-09-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='latitude',
            field=models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='point',
            name='longitude',
            field=models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Долгота'),
        ),
    ]