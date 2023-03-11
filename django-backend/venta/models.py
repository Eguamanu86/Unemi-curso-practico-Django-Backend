from django.db import models
from inventario.models import Producto
from cliente.models import Cliente
# Create your models here.
class TipoPago(models.Model):
    codigo = models.CharField(max_length=10, verbose_name="Codigo", blank=True, null=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre", blank=True, null=True)
    monto = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Pago'
        verbose_name_plural = 'Tipo de Pagos'
        ordering = ('codigo',)


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=True, null=True)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.PROTECT, blank=True, null=True)
    numero = models.CharField(verbose_name="Número", max_length=10)
    fecha = models.DateTimeField(blank=True, null=True)
    subtotal = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    deleted_by = models.CharField(max_length=100, blank=True, null=True, editable=False)


    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ('-created_at',)

class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, blank=True, null=True)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(default=0, max_digits=10,decimal_places=2)
    subtotal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True, editable=False)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name = 'Venta detalle'
        verbose_name_plural = 'Venta detalles'
        ordering = ('created_at',)
