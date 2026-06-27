from django.urls import path
from . import views

url patterns = [
    path('', views.home, name='home'),
    }