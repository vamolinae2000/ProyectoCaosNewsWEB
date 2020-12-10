"""CaosNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from frontend import views
from API import views
#from core import *
from backend import views as views_backend
from django.conf.urls.static import static
from django.conf.urls import url
from core import static

#from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
#from .views import delete_view 
admin.autodiscover()

app_name = "users"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.Index),
    path('Usuario/', views_backend.Usuario),
    path('GuardarUsuario/', views_backend.GuardarUsuario),
    path('SubirFoto/', views_backend.SubirFoto),
    path('GuardarImagen/', views_backend.GuardarImagen),
    path('', views.MenuUsuario),
    path('MenuUsuario/', views.MenuUsuario),
    path('listar/', views_backend.listar),
    path('verImagen/<int:id>', views.verImagen),
    path('Periodista/', views_backend.Periodista),
    path('GuardarPeriodista/', views_backend.GuardarPeriodista),
    path('<id>/eliminar', views_backend.listar),
    path('listarP/', views_backend.listarP),
    path('login/', views_backend.login ),
    path('MenuAdmin/', views_backend.MenuAdmin),
    path('listarN/', views_backend.listarN),
    path('listadoPeriodista/', views_backend.listadoPeriodista),
    #path('api/v1', include('API.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', views_API.API_Usuario)
    #path("login/", views_core.login, name="login"),
    #path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #path('social-auth/', include('social_django.urls', namespace="social")),
    #path("", views.home, name="home"),
    
]
