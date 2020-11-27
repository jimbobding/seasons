from django.urls import path
from . import views 

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('subscription_detail/<subscriptions_id>', views.subscription_detail, name='subscription_detail'),
    path('subscription', views.subscription, name='subscription'),

    
]