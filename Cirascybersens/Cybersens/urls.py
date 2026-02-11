from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.Accueil_view, name='Accueil'),
]