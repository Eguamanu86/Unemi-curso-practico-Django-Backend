from django.db import models

class ProductoCategoria(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=10, blank=True, null=True)
    nombre = models.CharField(verbose_name="Categoria", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto Categoria'
        verbose_name_plural = 'Producto Categorias'

class Producto(models.Model):
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.PROTECT, blank=True, null=True)
    codigo = models.CharField(verbose_name="Código", max_length=20, blank=True, null=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=100, blank=True,null=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=1024, blank=True, null=True)
    stock_disponible = models.IntegerField(default=0, verbose_name="Disponible")
    stock_minimo = models.IntegerField(default=0, verbose_name="Stock Minimo")
    precio = models.DecimalField(default=0, decimal_places=2 , max_digits=8)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True, editable=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']
