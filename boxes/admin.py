from django.contrib import admin
from .models import Season, Box

# Register your models here.


class SeasonAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'season',
        'box_name',
        'price',
        'description',
        'size',
        'fruit',
        'veg',
        'image',
    )


admin.site.register(Season, SeasonAdmin)
admin.site.register(Box, BoxAdmin)
