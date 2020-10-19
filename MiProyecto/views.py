from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime

opcionesMenu = ["Inicio", "Servicios", "Contacto"]

def MiHome(request):
	temp = loader.get_template('Inicio.html')
	# context = {"opciones": opcionesMenu}
	# return HttpResponse(temp.render(context))
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

def Servicios(request):
	temp = loader.get_template('Servicios.html')
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

def Contacto(request):
	temp = loader.get_template('contacto.html')
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

# def contacto(request):
#     return HttpResponse("Contacto")
