from django.db import models

# Create your models here.

class ClienteGrupo(models.Model):
    codigo = models.CharField(max_length=20,verbose_name='Código',blank=True, null=True)
    nombre = models.CharField(max_length=100, verbose_name='Descripción', blank=True, null=True)

    def __str__(self):
        return f"{self.codigo}-{self.nombre}"
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['codigo']

class Cliente(models.Model):
    grupo = models.ForeignKey(ClienteGrupo, on_delete=models.PROTECT, blank=True, null=True)
    cedula = models.CharField(max_length=10, verbose_name="cedula", blank=True, null=True)
    nombres = models.CharField(max_length=100, verbose_name="nombres", blank=True, null=True, editable=False)
    nombre = models.CharField(max_length=50,verbose_name="nombre")
    apellido = models.CharField(max_length=50, verbose_name="apellido")
    direccion = models.CharField(max_length=1024, verbose_name="direccion", blank=True, null=True)
    ciudad = models.CharField(max_length=50, verbose_name="ciudad", blank=True, null=True)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    deleted_by = models.CharField(max_length=100, blank=True, null=True, editable=False)

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('-created_at',)

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()

        if self.apellido:
            self.apellido = self.apellido.upper()

        self.nombres = f"{self.nombre} {self.apellido}"

        super(Cliente, self).save(force_insert, force_update, using)
