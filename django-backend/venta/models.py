from django.db import models
from inventarios.models import Producto

# Create your models here.

class TipoPago(models.Model):
    codigo = models.CharField(verbose_name="Codigo", blank=True, null=True)
    nombre = models.CharField(verbose_name="Nombre", blank=True, null=True)
    monto = models.DecimalField(default=0, decimal_places=2)

    def __str__(self):
        return f"{self.nombre}"


class Venta(models.Model):
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.PROTECT, blank=True, null=True)
    numero = models.CharField(verbose_name="Número", max_length=10)
    fecha = models.DateTimeField(blank=True, null=True)
    subtotal = models.DecimalField(default=0, decimal_places=2)
    impuesto = models.DecimalField(default=0, decimal_places=2)
    total = models.DecimalField(default=0, decimal_places=2)



class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, blank=True, null=True)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(default=0, decimal_places=2)
    subtotal = models.DecimalField(default=0, decimal_places=2)
    impuesto = models.DecimalField(default=0, decimal_places=2)
    total = models.DecimalField(default=0, decimal_places=2)
