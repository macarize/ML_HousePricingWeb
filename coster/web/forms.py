from django import forms
from .models import *

class consultantForm(forms.Form):
    space = forms.FloatField()
    floor = forms.IntegerField()
    rooms = forms.IntegerField()
    year = forms.IntegerField()

class signupForm(forms.Form):
    id = forms.CharField()
    pw = forms.CharField()
    name = forms.CharField()
