from django.urls import path
from .views import CarListView, CarDetailView

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('car/<str:slug>/', CarDetailView.as_view(), name='car-detail'),
]
