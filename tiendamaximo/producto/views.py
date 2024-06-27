from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def bienvenida(request):
    return HttpResponse("hola bienvenido a tienda maximo.")