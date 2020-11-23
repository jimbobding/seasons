from django.contrib import admin
from .models import Subscriptions, Size


# Register your models here.

class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'description',
            'price',
            'price_per_box',
            'image',
            'months',
            'fruit',
            'vegetables',
        )


class SizeAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'price',
            'price_per_box',

        )


admin.site.register(Size, SizeAdmin)
admin.site.register(Subscriptions, SubscriptionsAdmin)
