from django.urls import path
from . import views  # Asumiendo que tus vistas están en empleados/views.py

urlpatterns = [
    path('', views.lista_empleados, name='lista_empleados'), # Esto coincide con la ruta vacía bajo /empleados/
    # Puedes agregar otros patrones de URL para la aplicación empleados aquí
]