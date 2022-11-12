from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from .forms import usuarioForm
from .models import TipoUsuario
from .models import PuntoTuristico
from .forms import puntoTuristicoForm
from .models import CategoriaTurismo
from .forms import categoriaTurismoForm
from .models import Evento
from .forms import eventoForm
from .models import CategoriaEvento
from .forms import categoriaEventoForm
import json
from json import dumps
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenido a Turismo</h1>")
def turi(request):
    return render(request, 'paginas/turi.html')
def login(request):
    usuarios = Usuarios.objects.all()
    busqueda = request.GET.get("Buscar")
    if busqueda:
        usuarios = Usuarios.objects.filter(
            Q(id__icontains = busqueda) |
            Q(nombre__icontains = busqueda)
        ).distinct()
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
    busqueda = request.GET.get("Buscar")
    if busqueda:
        puntos = PuntoTuristico.objects.filter(
            Q(puntoID__icontains = busqueda) |
            Q(puntoNombre__icontains = busqueda) |
            Q(puntoCatID__catturdescrip__iexact = busqueda)
        ).distinct()
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

def tipoPunto(request):
    tipoPuntos = CategoriaTurismo.objects.all()
    return render(request, 'tipoPuntos/categoriaPunto.html', {'tipoPuntos': tipoPuntos})
def creartipoPunto(request):
    formulario = categoriaTurismoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categoriaPunto')
    return render(request, 'tipoPuntos/crearTipoPunto.html', {'formulario': formulario})
def modificartipoPunto(request, catturid):
    tipoPuntos = CategoriaTurismo.objects.get(catturid=catturid)
    formulario = categoriaTurismoForm(request.POST or None, request.FILES or None, instance=tipoPuntos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return  redirect('categoriaPunto')
    return render(request, 'tipoPuntos/modificarTipoPunto.html', {'formulario': formulario})
def eliminarTipoPunto(request, catturid):
    tipoPuntos = CategoriaTurismo.objects.get(catturid=catturid)
    tipoPuntos.delete()
    return redirect('categoriaPunto')
def eventos(request):
    eventos = Evento.objects.all()
    busqueda = request.GET.get("Buscar")
    if busqueda:
        eventos = Evento.objects.filter(
            Q(eventoid__icontains = busqueda) |
            Q(eventonombre__icontains = busqueda) |
            Q(eventocategid__cateventodescrip__iexact = busqueda)
        ).distinct()
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
#
def tipoEvento(request):
    tipoEventos = CategoriaEvento.objects.all()
    return render(request, 'tipoEventos/categoriaEvento.html', {'tipoEventos': tipoEventos})
def creartipoEvento(request):
    formulario = categoriaEventoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categoriaEvento')
    return render(request, 'tipoEventos/crearTipoEvento.html', {'formulario': formulario})
def modificartipoEvento(request, cateventoid):
    tipoEventos = CategoriaEvento.objects.get(cateventoid=cateventoid)
    formulario = categoriaEventoForm(request.POST or None, request.FILES or None, instance=tipoEventos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return  redirect('categoriaEvento')
    return render(request, 'tipoEventos/modificarTipoEvento.html', {'formulario': formulario})
def eliminarTipoEvento(request, cateventoid):
    tipoEvento = CategoriaEvento.objects.get(cateventoid=cateventoid)
    tipoEvento.delete()
    return redirect('categoriaEvento')
#
def obtenerUsuarioID(request, id):
    variable = 3
    usuarios = Usuarios.objects.get(id=id)
    dicci = f'{{"name" : {usuarios.nombre}, "Correo" : {usuarios.correo}}}'
    #a = json.dumps(dicci)
    return HttpResponse(json.dumps(dicci),content_type="application/json")
    #return HttpResponse(dicci)
def mostrarPuntosTuristicos(request):
    informacion = PuntoTuristico.objects.all()
    diccionario = [model for model in informacion.values()]
    return HttpResponse(json.dumps(diccionario),content_type="application/json")
def mostrarUsuarios(request):
    informacion = Usuarios.objects.all()
    diccionario = [model for model in informacion.values()]
    return HttpResponse(json.dumps(diccionario),content_type="application/json")
def mostrarEvento(request):
    informacion = Evento.objects.all()
    diccionario = [model for model in informacion.values()]
    return HttpResponse(json.dumps(diccionario),content_type="application/json")
def mostrarTipoUsuario(request):
    informacion = TipoUsuario.objects.all()
    diccionario = [model for model in informacion.values()]
    return HttpResponse(json.dumps(diccionario),content_type="application/json")
