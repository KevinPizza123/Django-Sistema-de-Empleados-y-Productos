from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Producto
from .forms import ProductoForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos') # Redirige a la lista después de guardar
    else:
        form = ProductoForm()
    return render(request, 'inventario/agregar_producto.html', {'form': form})

#clase
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
#API
@api_view(['GET'])
def producto_list(request):
    """
    Lista todos los productos.
    """
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)