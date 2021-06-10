from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import User, Address


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Created account for {username}')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/user_register.html', {'form': form})


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
            'driver_license_id', 'personal_id',]


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['city', 'street', 'house_number', 'flat_number', 'zip_code']


@login_required
def profile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        address_form = AddressForm(request.POST, instance=request.user.address)
        if update_form.is_valid() and address_form.is_valid():
            update_form.address = address_form
            address_form.save()
            update_form.save()
            return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        address_form = AddressForm(instance=request.user.address)
    context = {
        'update_form': update_form,
        'address_form': address_form
    }
    return render(request, 'user/user_profile.html', context)
