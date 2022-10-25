from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from .forms import usuarioForm
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