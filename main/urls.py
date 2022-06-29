from django.urls import path
from .views import HomeView, DrinkListView, DrinkCreateView, PubCreateView, PubListView, DrinkUpdateView, DrinkDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('drinks/', DrinkListView.as_view(), name='drinks'),
    path('drinks/new/', DrinkCreateView.as_view(), name='drink.new'),
    path('drinks/<int:pk>/edit/', DrinkUpdateView.as_view(), name='drink.edit'),
    path('drinks/delete/<int:pk>/', DrinkListView.as_view(), name='drink.delete'),
    path('pubs/', PubListView.as_view(), name='pubs'),
    path('pubs/new/', PubCreateView.as_view(), name='new_pub'),
]