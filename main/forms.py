from django import forms
from .models import Bar


class BarForm(forms.ModelForm):
    class Meta:
        model = Bar
        fields = ('__all__')

