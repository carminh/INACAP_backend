from django.shortcuts import render
from datetime import datetime

def index(request):
    fecha = datetime.now()
    contexto = {'fecha': fecha}
    return render(request, 'miapp/info.html', contexto )