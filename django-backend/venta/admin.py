from django.contrib import admin
# Register your models here.
from .models import *

# Register your models here.
admin.site.register(TipoPago)

class ItemVentaDetalleInline(admin.TabularInline):
    model = VentaDetalle
    extra = 0

class VentaAdmin(admin.ModelAdmin):
    inlines = [ItemVentaDetalleInline]
    list_display = (
        'numero',
        'fecha',
        'cliente',
        'tipo_pago',
        'subtotal',
        'impuesto',
        'total'
    )
    list_per_page = 20
    ordering = ('-created_at',)
    search_fields = ('numero','cliente', 'fecha')
    list_filter = (
        'estado',
    )

admin.site.register(Venta,VentaAdmin)
