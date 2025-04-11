from django.urls import path
from . import views

urlpatterns = [
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    # Aquí puedes agregar más URLs para la aplicación inventario
]