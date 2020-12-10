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
from django.contrib import messages 

# Create your views here.


def MenuUsuario(request):

    return render(request,'menuUsuario.html')

def Index(request):
    imagenes=models.Imagen.objects.all()
    datos={"imagenes":imagenes}
    return render(request, 'index.html', datos)

def verImagen(request, id):
    imagen=models.Imagen.objects.get(idImagen=id)
    datos={"imagen":imagen}
    return render(request, 'verImagen.html', datos)

