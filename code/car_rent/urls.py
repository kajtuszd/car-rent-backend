from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='car_rent-home'),
    path('about/', views.about, name='car_rent-about'),
]
