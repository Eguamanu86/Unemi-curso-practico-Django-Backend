from django.db import models

# Create your models here.

class ClienteGrupo(models.Model):
    codigo = models.CharField(blank=True, null=True)
    nombre = models.CharField(blank=True, null=True)


class Cliente(models.Model):
    grupo = models.ForeignKey(ClienteGrupo, blank=True, null=True)
    cedula = models.CharField(verbose_name="cedula", blank=True, null=True)
    nombres = models.CharField(verbose_name="nombres", blank=True, null=True)
    nombre = models.CharField(verbose_name="nombre", blank=True, null=True)
    apellido = models.CharField(verbose_name="apellido", blank=True, null=True)
    direccion = models.CharField(verbose_name="direccion", blank=True, null=True)
    ciudad = models.CharField(verbose_name="ciudad", blank=True, null=True)
