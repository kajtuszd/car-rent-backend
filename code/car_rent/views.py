from django.shortcuts import render


def home(request):
    return render(request, 'car_rent/home.html')


def about(request):
    return render(request, 'car_rent/about.html')
