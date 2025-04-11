from django.shortcuts import render
from .models import PerfilEmpleado  # Importa el modelo PerfilEmpleado

def lista_empleados(request):
    empleados = PerfilEmpleado.objects.all()  # Obtiene todos los objetos PerfilEmpleado
    context = {'empleados': empleados}
    return render(request, 'empleados/lista_empleados.html', context)