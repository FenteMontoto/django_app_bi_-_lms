from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    
    return render(request,'gestion_usuarios/login.html',({"title":"Home"}))

def home(request):
    

    return render(request,'gestion_usuarios/home.html',({"title":"Home"}))

def formacion(request):
    
    return render(request,'gestion_usuarios/formacion.html',({"title":"Formación"}))

def mensajeria(request):
    
    return render(request,'gestion_usuarios/mensajeria.html',({"title":"Mensajería"}))

def mi_actividad(request):
    
    return render(request,'gestion_usuarios/mi_actividad.html',({"title":"Mi actividad"}))