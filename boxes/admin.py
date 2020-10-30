from django.contrib import admin
from .models import Season, Boxes

# Register your models here.


class SeasonAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


class BoxesAdmin(admin.ModelAdmin):
    list_display = (
        'season',
        'box_name',
        'price',
        'description',
        'size',
        'fruit',
        'veg',
        'image_url',
        'image',
    )


admin.site.register(Season, SeasonAdmin)
admin.site.register(Boxes, BoxesAdmin)
