from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('drinks/', views.DrinkListView.as_view(), name='drinks'),
    path('drinks/detail/<int:pk>/', views.DrinkDetailView.as_view(), name="drink.detail"),
    path('drinks/new/', views.DrinkCreateView.as_view(), name='drink.new'),
    path('drinks/edit/<int:pk>/', views.DrinkUpdateView.as_view(), name='drink.edit'),
    path('drinks/delete/<int:pk>/', views.DrinkDeleteView.as_view(), name='drink.delete'),
    path('pubs/', views.PubListView.as_view(), name='pubs'),
    path('pubs/detail/<int:pk>/', views.PubDetailView.as_view(), name="pub.detail"),
    path('pubs/new/', views.PubCreateView.as_view(), name='pub.new'),
    path('pubs/edit/<int:pk>/', views.PubUpdateView.as_view(), name='pub.edit'),
    path('pubs/delete/<int:pk>/', views.PubDeleteView.as_view(), name='pub.delete'),
]