from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Drink


class HomeView(TemplateView):
    template_name = 'main/index.html'


class DrinkListView(ListView):
    model = Drink
    queryset = Drink.objects.all().order_by('name')
    template_name = 'main/drinks.html'
