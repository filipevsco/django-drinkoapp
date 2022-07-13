from django import forms
from .models import Pub, Drink


class PubForm(forms.ModelForm):
    class Meta:
        model = Pub
        fields = ['name', 'description', 'rate', 'image']
        

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'bar', 'description', 'rate', 'image']
