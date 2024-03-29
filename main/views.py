from django.contrib.auth.decorators import login_required
from .models import Drink, Pub
from .forms import PubForm, DrinkForm
from django.views.generic import (
    TemplateView, ListView,
    CreateView, UpdateView,
    DeleteView, DetailView
    )
    
    
class HomeView(TemplateView):
    template_name = 'main/index.html'


class PubListView(ListView):
    model = Pub
    queryset = Pub.objects.all().order_by('name')
    template_name = 'main/pubs.html'
    context_object_name = 'pubs'
    paginate_by = 3


class PubCreateView(CreateView):
    model = Pub
    form_class = PubForm
    success_url = "/pubs/"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super(PubCreateView, self).form_valid(form)


class PubUpdateView(UpdateView):
    model = Pub
    form_class = PubForm
    success_url = "/pubs/"


class PubDeleteView(DeleteView):
    model = Pub
    success_url = "/pubs/"


class DrinkListView(ListView):
    model = Drink
    queryset = Drink.objects.all().order_by('name')
    template_name = 'main/drinks.html'
    context_object_name = 'drinks'
    pagination = 3


class DrinkCreateView(CreateView):
    model = Drink
    form_class = DrinkForm
    success_url = "/drinks/"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super(DrinkCreateView, self).form_valid(form)


class DrinkUpdateView(UpdateView):
    model = Drink
    form_class = DrinkForm
    success_url = "/drinks/"


class DrinkDeleteView(DeleteView):
    model = Drink
    success_url = "/drinks/"


class PubDetailView(DetailView):
    template_name = "main/detail_pub.html"
    context_object_name = "pub"
    model = Pub


class DrinkDetailView(DetailView):
    template_name = "main/detail_drink.html"
    context_object_name = "drink"
    model = Drink

