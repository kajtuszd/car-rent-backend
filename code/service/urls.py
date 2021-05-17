from django.urls import path
from .views import ServiceListView, ServiceDetailView


urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('service/<str:slug>/', ServiceDetailView.as_view(), name='service-detail'),
]
