from frontend.models import Categoria
from frontend.models import Usuario
from frontend.models import Periodista
from frontend.models import Imagen
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PeriodistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodista
        fields = '__all__'

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'
