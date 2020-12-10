from rest_framework import routers

from .viewsets import CategoriaViewSet
from .viewsets import UsuarioViewSet
from .viewsets import ImagenViewSet
from .viewsets import PeriodistaViewSet



router = routers.SimpleRouter()
router.register('Categoria', CategoriaViewSet)
router.register('Usuario', UsuarioViewSet)
router.register('Imagen', ImagenViewSet)
router.register('Periodista', PeriodistaViewSet)

urlpatterns = router.urls