from django.urls import path
from .views import ServiceListView, ServiceDetailView
from .forms import create_form

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('service/<str:slug>/', ServiceDetailView.as_view(), name='service'
                                                                  '-detail'),
    path('new/', create_form, name='service-form'),
]
