from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('turi', views.turi, name='turi'),
    path('login', views.login, name='login'),
    path('crear', views.crear, name='crearUsuario'),
    path('eventos', views.eventos, name='eventos'),
    path('eventos', views.eventos, name='eventos'),
    path('eliminar/<int:id>',views.eliminarUsuario, name="eliminar"),
    path('inicio/modificar/<int:id>',views.modificar, name="modificar"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)