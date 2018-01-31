from django.urls import path
from apps.equipoideal.views import index

app_name = 'equipoideal'
urlpatterns = [
    path('', index),
]
