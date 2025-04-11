from django.contrib import admin
from .models import Producto  # Importa tu modelo Producto

admin.site.register(Producto)  # Registra el modelo Producto con la administración