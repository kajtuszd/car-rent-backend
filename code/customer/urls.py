from django.urls import path
from .views import UserListView, UserDetailView


urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/<str:slug>/', UserDetailView.as_view(), name='user-detail'),
]
