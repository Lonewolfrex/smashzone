# tournaments/admin.py

from django.contrib import admin
from .models import Tournaments, Sport

class TournamentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'location')

admin.site.register(Tournaments, TournamentsAdmin)
admin.site.register(Sport)
