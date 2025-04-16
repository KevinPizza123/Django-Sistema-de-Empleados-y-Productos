from rest_framework import serializers
from .models import PerfilEmpleado

class PerfilEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilEmpleado
        fields = '__all__'  # Esto incluye todos los campos de tu modelo PerfilEmpleado



        