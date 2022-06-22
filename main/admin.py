from django.contrib import admin
from .models import Bar, Drink

admin.site.register(Drink)
admin.site.register(Bar)