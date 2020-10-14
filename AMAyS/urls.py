"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AMAyS import views
#from MiProyecto.views import login, contacto

urlpatterns = [
    path('',views.AMAyS_Inicio),
    path('inicio/',views.AMAyS_Inicio),
    path('institucional/',views.AMAyS_Institucional),
    path('servicios/',views.AMAyS_Servicios),
    path('contacto/',views.AMAyS_Contacto),
    path('revista/',views.AMAyS_Revista),
    path('ingresar/',views.AMAyS_Ingresar),
#    path('MiApp/',include('MiApp.urls')),
]
