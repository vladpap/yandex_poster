from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin

from .models import Image, Point


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ('get_thumbnail', )
    ordering = ('position', )


@admin.register(Point)
class SortablePointAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
