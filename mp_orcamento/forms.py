from django.forms import ModelForm

from .models import *

# FORMULARIO DE VENDEDORES
class FormVendedor(ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'


# FORMULARIO DE CLIENTE
class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


# FORMULARIO DE LINHA DE PRODUTOS
class FormLinha(ModelForm):
    class Meta:
        model = Linha
        fields = '__all__'


# FORMULARIO DE ALUMINIO
class FormAluminio(ModelForm):
    class Meta:
        model = Aluminio
        fields = '__all__'


# FORMULARIO DE ACESSORIOS
class FormAcessorio(ModelForm):
    class Meta:
        model = Acessorio
        fields = '__all__'


# FORMULARIO DE VIDROS
class FormVidro(ModelForm):
    class Meta:
        model = Vidro
        fields = '__all__'


# FORMULARIO DE PRODUTOS
class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


# FORMULARIO DE ORÇAMENTOS
class FormOrcamento(ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'


