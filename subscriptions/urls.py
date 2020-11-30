from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('subscription_detail/<season>/', views.subscription_detail,
                                         name='subscription_detail'),

]
