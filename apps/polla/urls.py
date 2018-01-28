from django.urls import path
from apps.polla.views import index, polla, resultados

app_name = 'polla'
urlpatterns = [
    path('', index),
    path('polla/<str:username>/', polla, name='polla'),
    path('resultados/<int:score>/', resultados, name='resultados'),
]
