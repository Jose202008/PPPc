from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime

opcionesMenu = [" Inicio ", " Servicios ", " Contacto "]

def contacto(request):
    return HttpResponse("Contacto")

def MiHome(request):
	temp = loader.get_template('Inicio.html')
	# context = {"opciones": opcionesMenu}
	# return HttpResponse(temp.render(context))
	return HttpResponse(temp.render({"opciones": opcionesMenu}))
