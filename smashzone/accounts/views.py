# smashzone/accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')  # Redirect to home page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
