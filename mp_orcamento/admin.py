from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Aluminio)
class AluminioAdmin(admin.ModelAdmin):
    pass

@admin.register(Acessorio)
class AcessorioAdmin(admin.ModelAdmin):
    pass

@admin.register(Vidro)
class VidroAdmin(admin.ModelAdmin):
    pass

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Linha)
class LinhaAdmin(admin.ModelAdmin):
    pass