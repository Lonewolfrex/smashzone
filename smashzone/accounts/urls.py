from django.urls import path
from .views import register_view
from .views import UserList, UserDetail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_view, name='register'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
