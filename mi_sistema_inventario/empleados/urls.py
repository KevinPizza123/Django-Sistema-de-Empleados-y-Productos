from django.urls import path, include
from rest_framework import routers
from . import views  # Asumiendo que tus vistas están en empleados/views.py

router = routers.DefaultRouter()
router.register(r'empleados', views.PerfilEmpleadoViewSet) # Registra el ViewSet para la ruta 'empleados'

urlpatterns = [
    path('', views.lista_empleados, name='lista_empleados'), # Esto coincide con la ruta vacía bajo /empleados/
    path('api/', include(router.urls)), # Incluye las rutas de la API REST
    # Puedes agregar otros patrones de URL para la aplicación empleados aquí
]