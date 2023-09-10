from django.contrib import admin

from .models import Point, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('thumbnail', )


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
