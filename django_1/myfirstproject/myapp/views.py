
from django.http import HttpResponse
from  datetime import datetime

# Create your views here.

def index(request):
    fecha = datetime.now()
    #nombre = input("Enter your name")
    #apellido= input("Enter your surname") 
    nombre = "Michelle"
    apellido= "Gamez" 
    html = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to the first try of Django!</h1>
        <p>This is a test for django</p>
        <p>Fecha: %s</p>
        <p>Welcome, %s %s</p>
        
        <p>\nDisfrutando la aventura...</p>
        <h4>by Carmen Herrera</h2>
    </body>
    </html>
    """ %(fecha, nombre, apellido)
    return HttpResponse(html)