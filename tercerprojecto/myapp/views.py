from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
    
def index(request):
    fecha = datetime.now()
    year = fecha.strftime("%Y")
    #diccionario con info del usuario
    usuario = {
        "nombre": "Carmen",
        "apellido": "Herrera",
        "edad": 19,
        "hobbies": ["Escuchar música", "Lectura", "Tomar solcito", "A deep convo"]
        #"hobbies": []
        
    }
    
    context = {
        "fecha": fecha,
        "año": year,
        "datosUsuario": usuario,
    }
    return render(request, "myapp/index.html", context)