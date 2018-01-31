from django.shortcuts import render
from apps.equipoideal.models import Formaciones
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = request.POST
        
        return render(request, 'equipoideal/jugadores.html', contexto)
    else:
        formaciones = Formaciones.objects.all()
        contexto = {'formaciones' : formaciones}
        return render(request, 'equipoideal/formacion.html', contexto)
