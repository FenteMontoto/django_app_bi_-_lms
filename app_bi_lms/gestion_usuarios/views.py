from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    
    return render(request,'gestion_usuarios/login.html')

def home(request):

    return render(request,'gestion_usuarios/home.html')

def formacion(request):
    
    return render(request,'gestion_usuarios/formacion.html')

def mensajeria(request):
    
    return render(request,'gestion_usuarios/mensajeria.html')

def mi_actividad(request):
    
    return render(request,'gestion_usuarios/mi_actividad.html')