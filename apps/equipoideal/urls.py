from django.urls import path
from apps.equipoideal.views import index, jugadores

app_name = 'equipoideal'
urlpatterns = [
    path('', index),
    path('jugadores/<int:formacion_id>', jugadores, name='jugadores'),
]
