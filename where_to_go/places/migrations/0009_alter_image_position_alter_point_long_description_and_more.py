# Generated by Django 4.2.4 on 2023-10-08 11:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_image_options_alter_point_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='point',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='point',
            name='short_description',
            field=models.TextField(blank=True, db_index=True, default='', verbose_name='Короткое описание'),
            preserve_default=False,
        ),
    ]
