from django.contrib import admin
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


from .models import Point, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ('thumbnail', )
    ordering = ('position', )


@admin.register(Point)
class SortablePointAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
