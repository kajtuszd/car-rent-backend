from django.views.generic import ListView, DetailView
from .models import Car, Engine


class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'cars'
    ordering = ['price_per_day']


class CarDetailView(DetailView):
    model = Car
