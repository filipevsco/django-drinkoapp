from django.urls import path
from .views import HomeView, DrinkListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('drinks/', DrinkListView.as_view(), name='drinks'),
]