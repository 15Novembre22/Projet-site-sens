from django.urls import path
from . import views

urlpatterns = [
    # C'est ici que le nom 'signaler_incident' est défini
    path('api/signaler/', views.signaler_incident, name='incident'),
]