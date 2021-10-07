from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    # ROTAS DE ORÇAMENTOS
    path('novo_orcamento/', novo_orcamento, name='novo_orcamento'),
    path('pesquisar_orcamento/', pesquisar_orcamento, name='pesquisar_orcamento'),
    path('excluir_orcamento/<int:id>', excluir_orcamento, name='excluir_orcamento'),

    # ROTAS DE CLIENTES
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_cliente/', listar_cliente, name='listar_cliente'),
    path('editar_cliente/<int:id>', editar_cliente, name='editar_cliente'),
    path('excluir_cliente/<int:id>', excluir_cliente, name='excluir_cliente'),

    # ROTAS DE PRODUTOS
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
    path('listar_produto/', listar_produto, name='listar_produto'),
    path('editar_produto/<int:id>', editar_produto, name='editar_produto'),
    path('excluir_produto/<int:id>', excluir_produto, name='excluir_produto'),

    # ROTAS DE VENDEDORES
    path('cadastrar_vendedor/', cadastrar_vendedor, name='cadastrar_vendedor'),
    path('listar_vendedor/', listar_vendedor, name='listar_vendedor'),
    path('editar_vendedor/<int:id>', editar_vendedor, name='editar_vendedor'),
    path('excluir_vendedor/<int:id>', excluir_vendedor, name='excluir_vendedor'),

    # ROTAS DE ALUMINIOS
    path('cadastrar_aluminio/', cadastrar_aluminio, name='cadastrar_aluminio'),
    path('editar_aluminio/<int:id>', editar_aluminio, name='editar_aluminio'),
    path('excluir_aluminio/<int:id>', excluir_aluminio, name='excluir_aluminio'),

    # ROTAS DE ACESSORIOS
    path('cadastrar_acessorio/', cadastrar_acessorio, name='cadastrar_acessorio'),
    path('editar_acessorio/<int:id>', editar_acessorio, name='editar_acessorio'),
    path('excluir_acessorio/<int:id>', excluir_acessorio, name='excluir_acessorio'),

    # ROTAS DE LINHA DE PRODUTOS
    path('cadastrar_linha_produto/', cadastrar_linha_produto, name='cadastrar_linha_produto'),
    path('editar_linha_produto/<int:id>', editar_linha_produto, name='editar_linha_produto'),
    path('excluir_linha_produto/<int:id>', excluir_linha_produto, name='excluir_linha_produto'),

    # ROTAS DE VIDROS
    path('cadastrar_vidro/', cadastrar_vidro, name='cadastrar_vidro'),
    path('editar_vidro/<int:id>', editar_vidro, name='editar_vidro'),
    path('excluir_vidro/<int:id>', excluir_vidro, name='excluir_vidro'),


]
