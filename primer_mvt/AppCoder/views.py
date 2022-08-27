from os import listxattr
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import familiares

# Create your views here.

def familiares(request):
    familiar=familiares(nombre_apellido="Ignacio Guerrero",dni="43441681", cumpleaños='2001-05-29')
    diccionario={'nombre':familiar.nombre_apelldo,'apellido':familiar.dni,'cumpleaños':familiar.cumpleaños}
    familiar.save()
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)