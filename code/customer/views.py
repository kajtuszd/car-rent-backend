from django.views.generic import ListView, DetailView
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    ordering = ['last_name']


class UserDetailView(DetailView):
    model = User
