from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# opcionesMenu = ["Inicio", "Institucional", "Servicios", "Contacto", "Revista", "Ingresar"]
opcionesMenu = ["Inicio", "Institucional", "Contacto", "Revista"]

def AMAyS_Inicio(request):
	temp = loader.get_template("AMAyS_Inicio.html")
	# context = {"opciones": opcionesMenu}
	# return HttpResponse(temp.render(context))
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

def AMAyS_Institucional(request):
	temp = loader.get_template("AMAyS_Institucional.html")
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

def AMAyS_Servicios(request):
	temp = loader.get_template("AMAyS_Servicios.html")
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

def AMAyS_Contacto(request):
	temp = loader.get_template("AMAyS_Contacto.html")
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

def AMAyS_Revista(request):
	temp = loader.get_template("AMAyS_Revista.html")
	return HttpResponse(temp.render({"opciones": opcionesMenu}))

def AMAyS_Ingresar(request):
	temp = loader.get_template("AMAyS_Ingresar.html")
	return HttpResponse(temp.render({"opciones": opcionesMenu}))
