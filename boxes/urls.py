from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_boxes, name='boxes'),
    path('<season_id>/', views.season_detail, name='season_detail'),
]

