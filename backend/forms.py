from django.forms import ModelForm
from .models import frontend


class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password']

class FormPeriodista(ModelForm):
    class Meta:
        model = Periodista
        fields = ['nombre', 'email', 'password', 'idperiodista']

class FormImagen(ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen', 'idImagen', 'texto', 'nombre', 'fechaRegistro', 'categoria', 'periodista']