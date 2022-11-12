from django.contrib import admin
from .models import Usuarios
from .models import PuntoTuristico
from .models import TipoUsuario
from .models import CategoriaTurismo
from .models import Evento
from .models import CategoriaEvento

admin.site.register(Usuarios)
admin.site.register(PuntoTuristico)
admin.site.register(TipoUsuario)
admin.site.register(CategoriaTurismo)
admin.site.register(Evento)
admin.site.register(CategoriaEvento)


