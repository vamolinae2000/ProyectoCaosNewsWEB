from frontend.models import Categoria
from frontend.models import Usuario
from frontend.models import Periodista
from frontend.models import Imagen
from rest_framework import viewsets
from .serializer import CategoriaSerializer
from .serializer import UsuarioSerializer
from .serializer import PeriodistaSerializer
from .serializer import ImagenSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

class PeriodistaViewSet(viewsets.ModelViewSet):
    queryset=Periodista.objects.all()
    serializer_class=PeriodistaSerializer

class ImagenViewSet(viewsets.ModelViewSet):
    queryset=Imagen.objects.all()
    serializer_class=ImagenSerializer