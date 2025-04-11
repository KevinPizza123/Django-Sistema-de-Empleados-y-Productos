from django.db import models
from django.contrib.auth.models import User  # Para relacionar con el empleado
from inventario.models import Producto

class Venta(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_impuesto = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) # Para la tasa actual

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta}"

class ItemVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Venta #{self.venta.id}"