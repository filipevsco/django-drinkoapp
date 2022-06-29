from django.urls import path
from .views import HomeView, DrinkListView, DrinkCreateView, PubCreateView, PubListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('drinks/', DrinkListView.as_view(), name='drinks'),
    path('drinks/new/', DrinkCreateView.as_view(), name='drink.new'),
    path('drinks/<int:id>/edit/', DrinkUpdateView.as_view(), name='drink.edit'),
    path('pubs/', PubListView.as_view(), name='pubs'),
    path('pubs/new/', PubCreateView.as_view(), name='new_pub'),
]