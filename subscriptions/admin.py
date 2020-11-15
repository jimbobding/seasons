from django.contrib import admin
from .models import Subscriptions


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


admin.site.register(Subscriptions, SubscriptionsAdmin)
