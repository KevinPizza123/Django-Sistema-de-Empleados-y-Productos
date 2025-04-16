from django.urls import path , include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet) # Registra el ViewSet para la ruta 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('api/', include(router.urls)), # Incluye las rutas de la API REST
    
]