from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    roles = forms.MultipleChoiceField(choices=Profile.ROLE_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', 'roles')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        profile = Profile(user=user, phone_number=self.cleaned_data['phone_number'], roles=self.cleaned_data['roles'])
        if commit:
            profile.save()
        return user
