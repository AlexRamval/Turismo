from django import forms
from .models import Usuarios
from .models import PuntoTuristico
from .models import Evento
from .models import CategoriaTurismo
from .models import CategoriaEvento

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class puntoTuristicoForm(forms.ModelForm):
    class Meta:
        model = PuntoTuristico
        fields = '__all__'

class categoriaTurismoForm(forms.ModelForm):
    class Meta:
        model = CategoriaTurismo
        fields = '__all__'

class eventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class categoriaEventoForm(forms.ModelForm):
    class Meta:
        model = CategoriaEvento
        fields = '__all__'