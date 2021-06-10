from django import forms
from django.forms import fields, models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Payment
from car.models import Car


class ServiceCreationForm(forms.ModelForm):
    rent_date = forms.DateTimeField(widget=forms.SelectDateWidget())
    return_date = forms.DateTimeField(widget=forms.SelectDateWidget())
    car = forms.ModelChoiceField(queryset=Car.objects.all())

    class Meta:
        model = Service
        fields = ('rent_date', 'return_date', 'car',)
        exclude = ('customer',)


class PaymentCreationForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_method',)


@login_required
def create_form(request):
    if request.method == 'POST':
        form_service = ServiceCreationForm(request.POST)
        form_payment = PaymentCreationForm(request.POST)
        if form_service.is_valid() and form_payment.is_valid() and request.user:
            payment_object = form_payment.save()
            service_object = form_service.save(commit=False)
            service_object.customer = request.user
            time_rent = service_object.return_date - service_object.rent_date
            service_object.payment = payment_object
            service_object.payment.amount = form_service.cleaned_data[
                                        'car'].price_per_day * time_rent.days
            payment_object.save()
            service_object.save()
            return redirect('profile')
    else:
        form_service = ServiceCreationForm()
        form_payment = PaymentCreationForm()
    return render(request, 'service/service_form.html', {'form1': form_service,
                                                         'form2': form_payment})
