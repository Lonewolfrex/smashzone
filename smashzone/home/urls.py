from django.urls import path
from .views import home_view, news_view, contact_view, login_view,tournaments_view

urlpatterns = [
    path('', home_view, name='home'),
    path('news/', news_view, name='news'),
    path('contact/', contact_view, name='contact'),
    path('login/', login_view, name='login'),
    path('tournaments/', tournaments_view, name='tournaments'),
]
