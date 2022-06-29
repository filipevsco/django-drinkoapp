from django import forms
from .models import Bar, Drink


class BarForm(forms.ModelForm):
    class Meta:
        model = Bar
        fields = ('__all__')

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('__all__')
