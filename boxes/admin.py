from django.contrib import admin
from .models import Season, Boxes, Category

# Register your models here.


class SeasonAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'fruit',
        'veg',
        'description',
        'image',
        'month_1',
        'month_2',
        'month_3',
    )


class BoxesAdmin(admin.ModelAdmin):
    list_display = (
        
        'box_name',
        'price',
        'description',
        'size',
        'fruit',
        'veg',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Season, SeasonAdmin)
admin.site.register(Boxes, BoxesAdmin)
admin.site.register(Category, CategoryAdmin)

