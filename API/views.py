from django.shortcuts import render
from rest_framework import ListApiView
from frontend import models
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from frontend import models
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import (get_object_or_404, 
render,  HttpResponseRedirect)
#LOGIN-LOGOUT-CREATE
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
#from app.forms import ContactForm

# Create your views here.

class UsuarioListApiview(ListApiView):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        return models.Usuario.objects.all()

def API_Usuario(request):
    usuarios=models.Usuario.objects.all

    datos={'Nombre':'Camila Ponce', ' Usuarios':usuarios}
    return render(request, 'api.html', datos)

