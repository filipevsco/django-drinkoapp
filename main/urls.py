from django.urls import path
from .views import HomeView, DrinkListView, BarCreateView, BarListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('drinks/', DrinkListView.as_view(), name='drinks'),
    path('bars/', BarListView.as_view(), name='bars'),
    path('bars/new/', BarCreateView.as_view(), name='new_bar'),
]