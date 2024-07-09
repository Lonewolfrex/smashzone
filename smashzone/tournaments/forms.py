# tournaments/forms.py

from django import forms
from .models import Tournaments, Sport

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournaments
        fields = ['name', 'description', 'sports', 'start_date', 'end_date', 'location']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': '{{ min_date }}', 'max': '{{ max_date }}'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'min': '{{ min_date }}', 'max': '{{ max_date }}'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize sports field to display checkboxes
        self.fields['sports'].widget = forms.CheckboxSelectMultiple()
        self.fields['sports'].queryset = Sport.objects.all()
