from django import forms
from .models import Driver, Team

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'age', 'team']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'country']
