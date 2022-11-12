from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('turi', views.turi, name='turi'),
    path('login', views.login, name='login'),
    path('crear', views.crear, name='crearUsuario'),
    path('eliminar/<int:id>',views.eliminarUsuario, name="eliminar"),
    path('inicio/modificar/<int:id>',views.modificar, name="modificar"),
    path('vistaP', views.puntoTuristico, name='vistaP'),
    path('crearPunto', views.crearPunto, name='crearPunto'),
    path('puntoTuristico/modificarPunto/<int:puntoID>',views.modificarPunto, name="modificarPunto"),
    path('eliminarP/<int:puntoID>',views.eliminarPunto, name="eliminarPunto"),
    path('categoriaPunto', views.tipoPunto, name='categoriaPunto'),
    path('crearTipoPunto', views.creartipoPunto, name='crearTipoPunto'),
    path('tipoPuntos/ModificarTipoPunto/<int:catturid>',views.modificartipoPunto, name="ModificarTipoPunto"),
    path('eliminarTipoPunto/<int:catturid>',views.eliminarTipoPunto, name="eliminarTipoPunto"),
    path('eventos', views.eventos, name='eventos'),
    path('crearEvento', views.crearEvento, name='crearEvento'),
    path('eliminarE/<int:eventoid>',views.eliminarEvento, name="eliminarEvento"),
    path('eventos/modificarEvento/<int:eventoid>',views.modificarEvento, name="modificarEvento"),
    path('categoriaEvento', views.tipoEvento, name='categoriaEvento'),
    path('crearTipoEvento', views.creartipoEvento, name='crearTipoEvento'),
    path('tipoEventos/ModificarTipoEvento/<int:cateventoid>',views.modificartipoEvento, name="ModificarTipoEvento"),
    path('eliminarTipoEvento/<int:cateventoid>',views.eliminarTipoEvento, name="eliminarTipoEvento"),
    path('obtenerUsuarioID/<int:id>', views.obtenerUsuarioID, name="obtenerUsuarioID"),
    path('mostrarPuntosTuristicos', views.mostrarPuntosTuristicos, name="mostrarPuntosTuristicos"),
    path('mostrarUsuarios', views.mostrarUsuarios, name="mostrarUsuarios"),
    path('mostrarEvento', views.mostrarEvento, name="mostrarEvento"),
    path('mostrarTipoUsuario', views.mostrarTipoUsuario, name="mostrarTipoUsuario"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)