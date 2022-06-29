from django import forms
from .models import Pub, Drink


class PubForm(forms.ModelForm):
    class Meta:
        model = Pub
        fields = ('__all__')


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('__all__')
