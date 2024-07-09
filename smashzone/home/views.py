from django.shortcuts import render
from tournaments.models import Tournaments

def home_view(request):
    return render(request, 'home/home.html')

def news_view(request):
    return render(request, 'home/news.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def login_view(request):
    return render(request, 'home/login.html')

def tournaments_view(request):
    tournaments = Tournaments.objects.all()
    return render(request, 'tournaments/tournaments.html', {'tournaments': tournaments})
