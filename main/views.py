from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Drink, Bar
from .forms import BarForm

class HomeView(TemplateView):
    template_name = 'main/index.html'


class DrinkListView(ListView):
    model = Drink
    queryset = Drink.objects.all().order_by('name')
    template_name = 'main/drinks.html'


class BarListView(ListView):
    model = Bar
    queryset = Bar.objects.all().order_by('name')
    template_name = 'main/bars.html'
    context_object_name = 'bars'


class BarCreateView(CreateView):
    model = Bar
    form_class = BarForm
    success_url = "/bars/"