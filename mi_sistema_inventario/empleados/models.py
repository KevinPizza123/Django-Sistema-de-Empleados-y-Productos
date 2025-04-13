from django.db import models
from django.contrib.auth.models import User

class PerfilEmpleado(models.Model):
    #usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_de_cedula = models.CharField(max_length=20, unique=True)  # Asumiendo que la cédula es única
    fecha_nacimiento = models.DateField(null=True, blank=True)  # Permite que sea opcional
    hijos = models.IntegerField(default=0, null=True, blank=True)  # Permite que sea opcional
    ESTADO_CIVIL_CHOICES = [
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo'),
        ('union_libre', 'Unión Libre'),
        ('otro', 'Otro'),
    ]
    estado_civil = models.CharField(
        max_length=20,
        choices=ESTADO_CIVIL_CHOICES,
        default='soltero',
        null=True,
        blank=True
    )
    correo = models.EmailField(max_length=254, unique=True)
    numero_de_telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"  # Muestra el nombre y apellido en lugar del username