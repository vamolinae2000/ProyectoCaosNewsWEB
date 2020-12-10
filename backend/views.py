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

def Usuario(request):
    #Esto es para llamar los usuarios de la base de datos y poder ponerlos en una tabla
    usuarios=models.Usuario.objects.all

    datos={'Nombre':'Camila Ponce', ' Usuarios':usuarios}
    return render(request, 'usuario.html', datos)

def GuardarUsuario(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        password=request.POST.get('password')

        nuevoUsuario=models.Usuario()
        nuevoUsuario.nombre=nombre
        nuevoUsuario.email=email
        nuevoUsuario.password=password

        nuevoUsuario.save()

    return HttpResponseRedirect('/MenuUsuario/')

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
            return render(request,"MenuAdmin.html", {'form': form})


    # Si llegamos al final renderizamos el formulario
    return render(request,"login.html", {'form': form})
def MenuAdmin(request):
    return render(request,'MenuAdmin.html')





def eliminar(request,id):
    periodista=Periodista.objects.get(idperiodista=id)
    periodista.delete()
    return HttpResponse("eliminado")

def edit(request, id_periodista):
    # Recuperamos la instancia de la persona
    instancia = models.Periodista.objects.get(idperiodista=id_periodista)

    # Creamos el formulario con los datos de la instancia
    form = FormPeriodista(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = FormPeriodista(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "core/edit.html", {'form': form})
    
def email (request):
    asunto = 'Gracias por registrarse en nuestro sitio' 
    mensaje = 'significa un mundo para nosotros' 
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = ['receiver@gmail.com',]

    send_mail (asunto, mensaje, email_from, recipient_list)
    return redirect ('redirigir a una nueva página')



def Periodista(request):
    #Esto es para llamar los usuarios de la base de datos y poder ponerlos en una tabla
    periodistas=models.Periodista.objects.all

    datos={'Nombre':'Camila Ponce', ' Periodista':periodistas}
    return render(request, 'periodista.html', datos)

def GuardarPeriodista(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        password=request.POST.get('password')
        idperiodista=request.POST.get('idperiodista')

        nuevoPeriodista=models.Periodista()
        nuevoPeriodista.nombre=nombre
        nuevoPeriodista.email=email
        nuevoPeriodista.password=password
        nuevoPeriodista.idperiodista=idperiodista


        nuevoPeriodista.save()

    return HttpResponseRedirect('/Periodista/')

def SubirFoto(request):
    categorias=models.Categoria.objects.all()
    periodistas=models.Periodista.objects.all()
    datos={"categorias":categorias, "periodistas": periodistas}
    return render(request, 'subirFoto.html', datos)

def GuardarImagen(request):

    if request.method=='POST':
        imagen=request.FILES['imagen']
        idImagen=request.POST['idImagen']
        texto=request.POST['texto']
        nombre=imagen.name
        fechaRegistro=request.POST['fecha']
        categoria=request.POST['categoria']
        periodista=request.POST['periodista']

        #guardar el archivo en el directorio
        arch=FileSystemStorage()

        arch.save(imagen.name, imagen)

        #sacamos la categoria desde la BD
        c=models.Categoria.objects.get(idCategoria=categoria)
        p=models.Periodista.objects.get(idperiodista=periodista)
        #Guarda los datos en la BD
        cate=models.Imagen(idImagen=idImagen, texto=texto, nombre=nombre, fechaRegistro=fechaRegistro, categoria=c, periodista=p)


        cate.save()
    
        
        return HttpResponseRedirect('/SubirFoto/')
    else:
        return HttpResponse('Error ')
def listar (request):

    listar = models.Usuario.objects.all()
    lis=models.Periodista.objects.all()
    foto=models.Imagen.objects.all()
    lis2 = {"Usuarios": listar, "Periodistas": lis, "Foto": foto}
    return render(request,'listar.html', lis2)
def listarP (request):

    lis=models.Periodista.objects.all()
    lis2 = {"Periodistas": lis,}
    return render(request,'listarP.html', lis2)

def listarN(request):
    imagenes=models.Imagen.objects.all()
    datos={"imagenes":imagenes}
    return render(request, 'listarN.html', datos)

def listadoPeriodista(request):
    lis=models.Periodista.objects.all()
    lis2 = {"Periodistas": lis,}
    return render(request, 'listadoPeriodista.html', lis2)

def verImagen(request, id):
    imagen=models.Imagen.objects.get(idImagen=id)
    datos={"imagen":imagen}
    return render(request, 'verImagen.html', datos)