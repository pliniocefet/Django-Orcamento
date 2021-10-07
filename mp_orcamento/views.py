from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *


# Create your views here.

@login_required()
def index(request):
    return render(request, 'mp_orcamento/index.html')

# VIEWS DE CLIENTES
@login_required()
def cadastrar_cliente(request):
    # TODO: Acrescentar menssagem de cliente cadastrado com sucesso ou falha
    lista_clientes = Cliente.objects.all()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cliente')
    else:
        form = FormCliente()
        context = {'lista_clientes': lista_clientes, 'form': form}
        return render(request, 'mp_orcamento/cadastrar_cliente.html', context)


@login_required()
def listar_cliente(request):
    # TODO: IMPLEMENTAR BUSCA DE CLIENTES ATUALIZAR A LISTA CONFORME DIGITA O TEXTO
    lista_clientes = Cliente.objects.all()
    context = {'lista_clientes': lista_clientes}
    return render(request, 'mp_orcamento/listar_cliente.html', context)

@login_required()
def editar_cliente(request, id):
    # TODO: Acrescentar menssagem de cliente alterado com sucesso ou falha
    lista_clientes = Cliente.objects.all()
    cliente = get_object_or_404(Cliente, id=id)
    form = FormCliente(request.POST or None, instance=cliente)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_cliente')
        else:
            context = {'form': form, 'lista_clientes': lista_clientes}
            form = FormCliente(request.POST or None, instance=cliente)
            return render(request, 'mp_orcamento/cadastrar_cliente.html', context)

    context = {'form': form, 'lista_clientes': lista_clientes}
    return render(request, 'mp_orcamento/cadastrar_cliente.html', context)


@login_required()
def excluir_cliente(request, id):
    # TODO: Acrescentar menssagem de confirmação de remoção de cliente
    # TODO: Acrescentar menssagem de cliente removido com sucesso ou falha
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('listar_cliente')


# VIEWS DE VENDEDORES
@login_required()
def cadastrar_vendedor(request):
    # TODO: Acrescentar menssagem de vendedor cadastrado com sucesso ou falha
    vendedores = Vendedor.objects.all()
    if request.method == 'POST':
        form = FormVendedor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vendedor')
    else:
        form = FormVendedor()
        return render(request, 'mp_orcamento/cadastrar_vendedor.html', {'form': form, 'vendedores': vendedores})


@login_required()
def listar_vendedor(request):
    # TODO: IMPLEMENTAR BUSCA DE VENDEDORES ATUALIZAR A LISTA CONFORME DIGITA O TEXTO
    lista_vendedores = Vendedor.objects.all()
    context = {'lista_vendedores': lista_vendedores}
    return render(request, 'mp_orcamento/listar_vendedor.html', context)


@login_required()
def editar_vendedor(request, id):
    # TODO: Acrescentar menssagem de vendedor alterado com sucesso ou falha
    vendedores = Vendedor.objects.all()
    vendedor = get_object_or_404(Vendedor, id=id)
    form = FormVendedor(request.POST or None, instance=vendedor)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('listar_vendedor')
        else:
            context = {'form': form, 'vendedor': vendedor, 'vendedores': vendedores}
            return render(request,'mp_orcamento/cadastrar_vendedor.html', context)

    context = {'form': form, 'vendedor': vendedor, 'vendedores': vendedores}
    return render(request, 'mp_orcamento/cadastrar_vendedor.html', context)

@login_required()
def excluir_vendedor(request, id):
    # TODO: Acrescentar menssagem de confirmação de remoção de vendedor
    # TODO: Acrescentar menssagem de vendedor removido com sucesso ou falha
    vendedor = get_object_or_404(Vendedor, pk=id)
    vendedor.delete()
    return redirect('listar_vendedor')


# VIEWS DE ALUMINIO
@login_required()
def cadastrar_aluminio(request):
    # TODO: Acrescentar menssagem de perfil cadastrado com sucesso ou falha
    lista_aluminios = Aluminio.objects.all()

    if request.method == "POST":
        form = FormAluminio(request.POST)

        if form.is_valid(): # se o fomulario for valido
            form.save()
            return redirect('listar_aluminio')
    else:
        form = FormAluminio() # se a requisição não for POST devolve o formulario prenchido
        context = {'lista_aluminios': lista_aluminios, 'form': form}
        return render(request, 'mp_orcamento/cadastrar_aluminio.html', context)

@login_required()
def listar_aluminio(request):
    # TODO: IMPLEMENTAR BUSCA DE ALUMINIOS ATUALIZAR A LISTA CONFORME DIGITA O TEXTO
    lista_aluminios = Aluminio.objects.all()
    context = {'lista_aluminios': lista_aluminios}
    return render(request, 'mp_orcamento/listar_aluminio.html', context)


@login_required()
def editar_aluminio(request, id):
    # TODO: Acrescentar menssagem de perfil alterado com sucesso ou falha
    lista_aluminios = Aluminio.objects.all() # busca todas as ocorrencias no banco
    aluminio_id = get_object_or_404(Aluminio, id=id) # busca pelo id no banco
    form = FormAluminio(instance=aluminio_id)

    if request.method == 'POST':
        form = FormAluminio(request.POST or None, instance=aluminio_id)
        if form.is_valid():
            form.save()
            return redirect('listar_aluminio')

    context = {'form': form, 'lista_aluminios': lista_aluminios}
    return render(request, 'mp_orcamento/cadastrar_aluminio.html', context)


@login_required()
# TODO: Acrescentar menssagem de confirmação de remoção de perfil
# TODO: Acrescentar menssagem de perfil removido com sucesso ou falha
def excluir_aluminio(request, id):
    aluminio = get_object_or_404(Aluminio, pk=id)
    aluminio.delete()
    return redirect('listar_aluminio')


# VIEWS DE ACESSORIOS
@login_required()
# TODO: Acrescentar menssagem de acessorio cadastrado com sucesso ou falha
def cadastrar_acessorio(request):
    lista_acessorios = Acessorio.objects.all()
    if request.method == 'POST':
        form = FormAcessorio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_acessorio')
    else:
        form = FormAcessorio()
        context = {'form': form, 'lista_acessorios': lista_acessorios}
        return render(request, 'mp_orcamento/cadastrar_acessorio.html', context)


@login_required()
def listar_acessorio(request):
    # TODO: IMPLEMENTAR BUSCA DE ACESSORIOS ATUALIZAR A LISTA CONFORME DIGITA O TEXTO
    lista_acessorios = Acessorio.objects.all()
    context = {'lista_acessorios': lista_acessorios}
    return render(request, 'mp_orcamento/listar_acessorio.html', context)


@login_required()
def editar_acessorio(request, id):
    # TODO: Acrescentar menssagem de acessorio alterado com sucesso ou falha
    lista_acessorios = Acessorio.objects.all()
    acessorio = get_object_or_404(Acessorio, id=id)
    form = FormAcessorio(request.POST or None, instance=acessorio)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('listar_acessorio')
        else:
            context = {'form': form, 'acessorio': acessorio, 'lista_acessorios': lista_acessorios}
            return render(request, 'mp_orcamento/cadastrar_acessorio.html', context)

    context = {'form': form, 'acessorio': acessorio, 'lista_acessorios': lista_acessorios}
    return render(request, 'mp_orcamento/cadastrar_acessorio.html', context)


@login_required()
# TODO: Acrescentar menssagem de confirmação de remoção de acessorio
# TODO: Acrescentar menssagem de acessorio removido com sucesso ou falha
def excluir_acessorio(request, id):
    acessorio = get_object_or_404(Acessorio, pk=id)
    acessorio.delete()
    return redirect('listar_acessorio')


# VIEWS DE LINHA DE PRODUTOS
@login_required()
def cadastrar_linha_produto(request):
    # TODO: Acrescentar menssagem de linha de produto cadastrado com sucesso ou falha
    linha_de_produtos = Linha.objects.all()
    if request.method == "POST":
        form = FormLinha(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_linha_produto')
    else:
        form = FormLinha()

    return render(request, 'mp_orcamento/cadastrar_linha_produto.html', {'form': form ,'linha_de_produtos': linha_de_produtos})

@login_required()
def listar_linha_produto(request):
    # TODO: IMPLEMENTAR BUSCA DE LINHA DE PRODUTOS ATUALIZAR A LISTA CONFORME DIGITA O TEXTO
    lista_linha_produtos = Linha.objects.all()
    context = {'lista_linha_produtos': lista_linha_produtos}
    return render(request, 'mp_orcamento/listar_linha_produto.html', context)


@login_required()
def editar_linha_produto(request, id):
    # TODO: Acrescentar menssagem de linha de produto alterado com sucesso ou falha
    linha_de_produtos = Linha.objects.all()
    linha = get_object_or_404(Linha, id=id)
    form = FormLinha(request.POST or None, instance=linha)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('listar_linha_produto')
        else:
            context = {'form': form, 'linha_de_produtos': linha_de_produtos}
            return render(request, 'mp_orcamento/cadastrar_linha_produto.html', context)

    context = {'form': form, 'linha_de_produtos': linha_de_produtos}
    return render(request, 'mp_orcamento/cadastrar_linha_produto.html', context)

@login_required()
def excluir_linha_produto(request, id):
    # TODO: Acrescentar menssagem de confirmação de remoção de linha de produto
    # TODO: Acrescentar menssagem de linha de produto removido com sucesso ou falha
    linha_produto = get_object_or_404(Linha, pk=id)
    linha_produto.delete()
    return redirect('listar_linha_produto')


# VIEWS DE VIDROS
@login_required()
def cadastrar_vidro(request):
    # TODO: Acrescentar menssagem de vidro cadastrado com sucesso ou falha
    lista_vidros = Vidro.objects.all()
    if request.method == "POST":
        form = FormVidro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_vidro')
    else:
        form = FormVidro()

    return render(request, 'mp_orcamento/cadastrar_vidro.html', {'form': form ,'lista_vidros': lista_vidros})

@login_required()
def listar_vidro(request):
    # TODO: IMPLEMENTAR BUSCA DE VIDROS ATUALIZAR A LISTA CONFORME DIGITA O TEXTO
    lista_vidros = Vidro.objects.all()
    context = {'lista_vidros': lista_vidros}
    return render(request, 'mp_orcamento/listar_vidro.html', context)



@login_required()
def editar_vidro(request, id):
    # TODO: Acrescentar menssagem de vidro alterado com sucesso ou falha
    lista_vidros = Vidro.objects.all() # lista todos os itens do banco
    vidro = get_object_or_404(Vidro, id=id)
    form = FormVidro(request.POST or None, instance=vidro)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_vidro')
        else:
            context = {'lista_vidros': lista_vidros, 'vidro': vidro, 'form': form}
            return render(request,'mp_orcamento/cadastrar_vidro.html', context)

    context = {'lista_vidros': lista_vidros, 'vidro': vidro, 'form': form}
    return render(request, 'mp_orcamento/cadastrar_vidro.html', context)

@login_required()
def excluir_vidro(request, id):
    # TODO: Acrescentar menssagem de confirmação de remoção de vidro
    # TODO: Acrescentar menssagem de vidro removido com sucesso ou falha
    vidro = get_object_or_404(Vidro, pk=id)
    vidro.delete()
    return redirect('listar_vidro')


# VIEWS DE PRODUTOS
@login_required()
def cadastrar_produto(request):
    # TODO: Acrescentar menssagem de produto cadastrado com sucesso ou falha
    lista_produtos = Produto.objects.all()
    if request.method == "POST":
        # instancia de outros formularios para ser exibidos na mesma pagina
        form = FormProduto(request.POST)
        # valida se todos os formularios estão preenchidos corretamente
        if form.is_valid():
            form.save() 
            return redirect('listar_produto')

    else:
        form = FormProduto()

    context = {
        'lista_produtos': lista_produtos,
        'form': form,
    }
    return render(request, 'mp_orcamento/cadastrar_produto.html', context)

@login_required()
def editar_produto(request, id):
    # TODO: Acrescentar menssagem de produto alterado com sucesso ou falha
    lista_produtos = Produto.objects.all()
    produto = get_object_or_404(Produto, id=id)
    form = FormProduto(request.POST or None, instance=produto)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_produto')
    else:
        context = {'lista_produtos': lista_produtos, 'produto': produto, 'form': form}
        return render(request, 'mp_orcamento/cadastrar_produto.html', context)


@login_required()
def listar_produto(request):
     # TODO: IMPLEMENTAR BUSCA DE PRODUTOS ATUALIZAR A LISTA CONFORME DIGITA O TEXTO
    lista_produtos = Produto.objects.all()
    context = {'lista_produtos': lista_produtos}
    return render(request, 'mp_orcamento/listar_produto.html', context)

@login_required()
def excluir_produto(request, id):
    # TODO: Acrescentar menssagem de confirmação de remoção de produto
    # TODO: Acrescentar menssagem de produto removido com sucesso ou falha
    produto = get_object_or_404(Produto, id=id)
    produto.delete()

    messages.info(request, 'Produto excluído com Sucesso!')
    
    return redirect('listar_produto')


# VIEWS DE ORÇAMENTOS
@login_required()
def novo_orcamento(request):
    # TODO: IMPLEMENTAR METODO PARA CRIAR NOVO ORÇAMENTO
    vendedores = Vendedor.objects.all()
    clientes = Cliente.objects.all()
    form_cliente = FormCliente()
    if request.method == 'POST':
        form_cliente = FormCliente(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('novo_orcamento')

    context = {'clientes': clientes, 'vendedores': vendedores, 'form_cliente': form_cliente}
    return render (request, 'mp_orcamento/novo_orcamento.html', context)

@login_required()
def pesquisar_orcamento(request):
    # TODO: FINALIZAR METODO DE PESQUISAR ORÇAMENTOS
    orcamentos = Orcamento.objects.all()
    context = {'orcamentos': orcamentos}
    return render (request, 'mp_orcamento/pesquisar_orcamento.html', context)

@login_required()
def editar_orcamento(request, id):
    # TODO: IMPLEMENTAR METODO EDITAR ORÇAMENTO
    """
    Ao clicar no botão editar orcamento, redirecionar o usuario para
    a pagina de novo orçamento já com o formulario preenchido com 
    os dados do orçamento
    """
    pass

@login_required()
def excluir_orcamento(request, id):
    # TODO: IMPLEMENTAR METODO EXCLUIR ORÇAMENTO
    orcamento = get_object_or_404(Orcamento, id=id)
    orcamento.delete()
    return redirect('pesquisar_orcamento')