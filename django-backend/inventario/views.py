from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView #, CreateView, UpdateView
from .models import *
# Create your views here.
class ProductoListView(LoginRequiredMixin,ListView):
    login_url = '/security/login'
    model = Producto
    template_name = 'inventario/productos.html'
    context_object_name = 'productos'
    paginate_by = 10


    def get_queryset(self, **kwargs):
        return Producto.objects.all().order_by('codigo')
