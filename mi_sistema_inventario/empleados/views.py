from django.shortcuts import render
from rest_framework import viewsets
from .models import PerfilEmpleado  # Importa el modelo PerfilEmpleado
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PerfilEmpleadoSerializer

def lista_empleados(request):
    empleados = PerfilEmpleado.objects.all()  # Obtiene todos los objetos PerfilEmpleado
    context = {'empleados': empleados}
    return render(request, 'empleados/lista_empleados.html', context)

#clase
class PerfilEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = PerfilEmpleado.objects.all()
    serializer_class = PerfilEmpleadoSerializer

#API
@api_view(['GET'])
def empleado_list(request):
    """
    Lista todos los empleados.
    """
    empleados = PerfilEmpleado.objects.all()
    serializer = PerfilEmpleadoSerializer(empleados, many=True)
    return Response(serializer.data)