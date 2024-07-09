# tournaments/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tournaments
from .forms import TournamentForm
from datetime import datetime, timedelta

class TournamentListView(ListView):
    model = Tournaments
    template_name = 'tournaments/tournament_list.html'
    context_object_name = 'tournaments'

class TournamentDetailView(DetailView):
    model = Tournaments
    template_name = 'tournaments/tournament_detail.html'
    context_object_name = 'tournament'

class TournamentCreateView(CreateView):
    model = Tournaments
    form_class = TournamentForm
    template_name = 'tournaments/tournament_form.html'
    success_url = reverse_lazy('tournament-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_date'] = datetime.now().strftime('%Y-%m-%d')
        context['max_date'] = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')
        return context

class TournamentUpdateView(UpdateView):
    model = Tournaments
    form_class = TournamentForm
    template_name = 'tournaments/tournament_form.html'
    success_url = reverse_lazy('tournament-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_date'] = datetime.now().strftime('%Y-%m-%d')
        context['max_date'] = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')
        return context

class TournamentDeleteView(DeleteView):
    model = Tournaments
    template_name = 'tournaments/tournament_confirm_delete.html'
    success_url = reverse_lazy('tournament-list')
