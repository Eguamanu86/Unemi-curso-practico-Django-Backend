from django.contrib import admin
# Register your models here.
from .models import *

# Register your models here.
admin.site.register(TipoPago)
admin.site.register(Venta)
admin.site.register(VentaDetalle)
