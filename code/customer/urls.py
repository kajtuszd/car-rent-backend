from django.urls import path
from .views import UserListView, UserDetailView
from .forms import register_user

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/<str:slug>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', register_user, name='register'),
]
