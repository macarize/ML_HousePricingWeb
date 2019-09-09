from django import forms
from .models import *

class consultantForm(forms.Form):
    space = forms.IntegerField()
    floor = forms.IntegerField()
    price = forms.CharField()
