from django.views.generic import ListView, DetailView
from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'services'
    ordering = ['rent_date']


class ServiceDetailView(DetailView):
    model = Service
