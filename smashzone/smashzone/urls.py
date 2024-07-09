from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('tournaments/', include('tournaments.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
