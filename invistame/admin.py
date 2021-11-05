from django.contrib import admin
from .models import Gasto, Contato, CategoriaContato, CategoriaGasto


admin.site.register(Gasto)
admin.site.register(Contato)
admin.site.register(CategoriaContato)
admin.site.register(CategoriaGasto)

