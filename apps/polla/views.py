from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.polla.forms import UsuarioForm
from apps.polla.models import Usuario, Partido, ParticipacionPolla
import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usr = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            usuario = len(Usuario.objects.filter(username=usr, password=pas))
            if usuario > 0:
                return redirect('login:polla', usr)
            else:
                print("Credenciales invalidas")

    else:
        form = UsuarioForm()

    return render(request, 'polla/login.html', {'form':form})

def polla(request, username):
    partidos = Partido.objects.all().order_by('id')
    contexto = {'partidos' : partidos}
    if request.method == 'POST':
        score = 0
        form = request.POST
        longitud = len(form)-1
        for x in range(0, longitud):
            i=form['a_partido_id={}'.format(x+1)]
            if i == str(partidos[x].resultado):
                score = score + 1
        user = Usuario.objects.get(username=username)
        fecha = datetime.datetime.now()
        formatedDate = fecha.strftime("%Y-%m-%d %H:%M:%S")
        participacion = ParticipacionPolla(usuario=user, score=score, fecha=formatedDate)
        participacion.save()
        return redirect('login:resultados', score)
    else:
        return render(request, 'polla/polla.html', contexto)

def resultados(request, score):
    partidos = Partido.objects.all().order_by('id')
    contexto = {'score' : score, 'partidos' : partidos}
    return render(request, 'polla/resultados.html', contexto)
