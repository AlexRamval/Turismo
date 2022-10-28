from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from .forms import usuarioForm
from .models import PuntoTuristico
from .forms import puntoTuristicoForm
from .models import Evento
from .forms import eventoForm
import json
from django.http import JsonResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenido a Turismo</h1>")
def turi(request):
    return render(request, 'paginas/turi.html')
def login(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'inicio/login.html', {'usuarios': usuarios})
def crear(request):
    formulario = usuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('login')
    return render(request, 'inicio/crearUsuario.html', {'formulario': formulario})
def modificar(request, id):
    usuarios = Usuarios.objects.get(id=id)
    formulario = usuarioForm(request.POST or None, request.FILES or None, instance=usuarios)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return  redirect('login')
    return render(request, 'inicio/modificar.html', {'formulario': formulario})
def eventos(request):
    return render(request, 'eventos/eventos.html')
def crearEvento(request):
    return render(request, 'eventos/crearEvento.html')
def eliminarUsuario(request, id):
    usuarios = Usuarios.objects.get(id=id)
    usuarios.delete()
    return redirect('login')
def puntoTuristico(request):
    puntos = PuntoTuristico.objects.all()
    return render(request, 'puntoTuristico/vistaP.html', {'puntos': puntos})
def crearPunto(request):
    formulario = puntoTuristicoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vistaP')
    return render(request, 'puntoTuristico/crearPunto.html', {'formulario': formulario})
def modificarPunto(request, puntoID):
    puntos = PuntoTuristico.objects.get(puntoID=puntoID)
    formulario = puntoTuristicoForm(request.POST or None, request.FILES or None, instance=puntos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return  redirect('vistaP')
    return render(request, 'puntoTuristico/modificarPunto.html', {'formulario': formulario})
def eliminarPunto(request, puntoID):
    puntos = PuntoTuristico.objects.get(puntoID=puntoID)
    puntos.delete()
    return redirect('vistaP')

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/eventos.html', {'eventos': eventos})
def crearEvento(request):
    formulario = eventoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('eventos')
    return render(request, 'eventos/crearEvento.html', {'formulario': formulario})
def modificarEvento(request, eventoid):
    eventos = Evento.objects.get(eventoid=eventoid)
    formulario = eventoForm(request.POST or None, request.FILES or None, instance=eventos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return  redirect('eventos')
    return render(request, 'eventos/modificarEvento.html', {'formulario': formulario})
def eliminarEvento(request, eventoid):
    eventos = Evento.objects.get(eventoid=eventoid)
    eventos.delete()
    return redirect('eventos')
def obtenerUsuarioID(request, id):
    variable = 3
    usuarios = Usuarios.objects.get(id=variable)
    dicci = f'{{"name" : {usuarios.nombre}, "Correo" : {usuarios.correo}}}'
    print(dicci)
    #return JsonResponse({dicci})
    return redirect(login)