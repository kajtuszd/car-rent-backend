from django.urls import path
from .views import (
    CarListView, CarDetailView, EngineListView, EngineDetailView
)

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('car/<str:slug>/', CarDetailView.as_view(), name='car-detail'),
    path('engines/', EngineListView.as_view(), name='engine-list'),
    path('engines/<str:slug>/', EngineDetailView.as_view(),
         name='engine-detail'),
]
