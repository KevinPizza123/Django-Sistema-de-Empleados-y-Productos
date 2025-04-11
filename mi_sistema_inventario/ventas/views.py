from django.shortcuts import render
from django.http import HttpResponse

def registrar_venta(request):
    """
    Vista para mostrar el formulario de registro de una nueva venta.
    """
    return HttpResponse("Página para registrar una nueva venta.")

def lista_ventas(request):
    """
    Vista para mostrar la lista de todas las ventas.
    """
    return HttpResponse("Página que muestra la lista de ventas.")

# Puedes agregar más vistas aquí según tus necesidades (por ejemplo, editar venta, ver detalles de venta, etc.)