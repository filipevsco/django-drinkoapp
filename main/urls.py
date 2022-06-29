from django.urls import path
from .views import HomeView, DrinkListView, DrinkCreateView, DrinkUpdateView, DrinkDeleteView, PubListView, PubCreateView, PubUpdateView, PubDeleteView

urlpatterns = [
    path('', 
    HomeView.as_view(), name='home'),
    path('drinks/', 
    DrinkListView.as_view(), name='drinks'),
    path('drinks/new/',
    DrinkCreateView.as_view(), name='drink.new'),
    path('drinks/edit/<int:pk>/',
    DrinkUpdateView.as_view(), name='drink.edit'),
    path('drinks/delete/<int:pk>/',
    DrinkDeleteView.as_view(), name='drink.delete'),
    path('pubs/', 
    PubListView.as_view(), name='pubs'),
    path('pubs/new/', 
    PubCreateView.as_view(), name='pub.new'),
    path('pubs/edit/<int:pk>/', 
    PubUpdateView.as_view(), name='pub.edit'),
    path('pubs/delete/<int:pk>/',
    PubDeleteView.as_view(), name='pub.delete'),
]