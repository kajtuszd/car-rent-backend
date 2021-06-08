from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserListView, UserDetailView
from .forms import register_user, profile

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/<str:slug>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', register_user, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/user_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/user_logout.html'), name='logout'),
]
