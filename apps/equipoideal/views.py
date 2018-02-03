from django.shortcuts import render, redirect
from apps.equipoideal.models import Formaciones, Jugador, Demarcacion

# Create your views here.
def index(request):
    if request.method == 'POST':
        formacion_id =  request.POST.__getitem__('formacion')
        return redirect('equipoideal:jugadores', formacion_id)
    else:
        formaciones = Formaciones.objects.all()
        contexto = {'formaciones' : formaciones}
        return render(request, 'equipoideal/formacion.html', contexto)

def jugadores(request, formacion_id):
    if request.method == 'POST':
        return render(request, 'equipoideal/resultados.html')
    else:
        formacion = Formaciones.objects.get(id=formacion_id)
        jugadores = Jugador.objects.all().order_by('id')
        arqueros = []
        defensas = []
        centrocampistas = []
        delanteros = []
        arquero = Demarcacion.objects.get(nombre='ARQUERO')
        defensa = Demarcacion.objects.get(nombre='DEFENSA')
        centrocampista = Demarcacion.objects.get(nombre='CENTROCAMPISTA')
        for jugador in jugadores:
            if jugador.demarcacion == arquero:
                arqueros.append(jugador)
            elif jugador.demarcacion == defensa:
                defensas.append(jugador)
            elif jugador.demarcacion == centrocampista:
                centrocampistas.append(jugador)
            else:
                delanteros.append(jugador)

        lst_defs = []
        print('cantidad de defensas: {}'.format(formacion.cantidad_defensas))
        cant_defs = formacion.cantidad_defensas
        for i in range(0, cant_defs):
            lst_defs.append(defensas)

        lst_cent = []
        print('cantidad de centros: {}'.format(formacion.cantidad_centrocampistas))
        for j in range(0, formacion.cantidad_centrocampistas):
            lst_cent.append(centrocampistas)

        lst_dela = []
        for k in range(0, formacion.cantidad_delanteros):
            lst_dela.append(delanteros)

        contexto = {'formacion' : formacion, 'arqueros' : arqueros,
        'lst_defs' : lst_defs, 'lst_cent' : lst_cent,
        'lst_dela' : lst_dela}

        return render(request, 'equipoideal/jugadores.html', contexto)
