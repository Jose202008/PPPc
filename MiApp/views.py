from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

# def login(request):
#     return HttpResponse("Bienvenido a mi blog")

def fecha_hora(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# def contacto(request):
#     return render(request, "MiProyecto/templates/homepage.html")