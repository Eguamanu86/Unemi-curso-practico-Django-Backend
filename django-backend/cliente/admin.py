from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(ClienteGrupo)

class ClienteAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Datos Personales', {
            'fields': [
                ('cedula',),
                ('nombre', 'apellido'),
                ('grupo', 'estado')
            ]
        }),
        ('Datos de direccion', {
            'fields': [
                ('direccion','ciudad')
            ]
        })
    ]

    list_display = (
        'cedula',
        'nombres',
        'grupo',
        'ciudad',
        'estado'
    )
    list_per_page = 20
    search_fields = ('cedula','nombres')
    list_filter = (
        'grupo',
        'estado'
    )

admin.site.register(Cliente, ClienteAdmin)
