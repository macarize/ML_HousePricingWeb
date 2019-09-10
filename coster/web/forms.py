from django import forms
from .models import *

class consultantForm(forms.Form):
    space = forms.IntegerField()
    floor = forms.IntegerField()
    price = forms.CharField()

# class loginForm(forms.Form):
#     id = forms.CharField()
#     pw = forms.CharField()