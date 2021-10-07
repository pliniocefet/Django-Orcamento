from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    endereco = models.CharField(max_length=128)
    telefone = models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    nome_vendedor = models.CharField(max_length=128)  # nome vendedor
    telefone_vendedor = models.CharField(max_length=30)  # telefone vendedor

    objects = models.Manager()

    def __str__(self):
        return self.nome_vendedor



# MODELS PARA LINHA DE PRODUTOS
class Linha(models.Model):
    codigo_linha = models.CharField(max_length=64)  # codigo
    descricao_linha = models.CharField(max_length=256)  # descrição

    objects = models.Manager()

    def __str__(self):
        return self.codigo_linha
    
    def __unicode__(self):
        return self.codigo_linha


class Aluminio(models.Model):
    codigo_aluminio = models.CharField(max_length=64)  # codigo
    descricao_aluminio = models.CharField(max_length=256)  # descricao
    peso_aluminio = models.FloatField()  # peso
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)  # linha

    objects = models.Manager()
    
    def __str__(self):
        return self.descricao_aluminio
    
    def __unicode__(self):
        return self.descricao_aluminio


class Acessorio(models.Model):
    codigo_acessorio = models.CharField(max_length=64)  # codigo
    descricao_acessorio = models.CharField(max_length=256)  # descricao
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)  # linha
    preco_acessorio = models.FloatField()  # preço

    objects = models.Manager()
    
    def __str__(self):
        return self.descricao_acessorio

    def __unicode__(self):
        return self.descricao_acessorio


class Vidro(models.Model):
    codigo_vidro = models.CharField(max_length=64)  # codigo
    descricao_vidro = models.CharField(max_length=256)  # descricao
    preco_vidro = models.FloatField()  # preço

    objects = models.Manager()

    def __str__(self):
        return self.descricao_vidro

    def __unicode__(self):
        return self.descricao_vidro


class Produto(models.Model):
    codigo_produto = models.CharField(max_length=64)  # codigo
    descricao_produto = models.CharField(max_length=256)  # descrição
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)  # vincular linha
    vidro = models.ForeignKey(Vidro, on_delete=models.CASCADE)  # vincular vidro
    aluminio = models.ForeignKey(Aluminio, on_delete=models.CASCADE)  # vincular aluminio
    acessorio = models.ForeignKey(Acessorio, on_delete=models.CASCADE)  # vincular acessorio
      
    def __str__(self):
        return self.descricao_produto

    def __unicode__(self):
        return self.descricao_produto


# MODELS PARA ORÇAMENTOS
class Orcamento(models.Model):
    """
    ITENS DO MODEL ORÇAMENTO
    * Nome do Cliente (ForeignKey Cliente)
    * Telefone do Cliente (ForeignKey Cliente)
    * Endereço do Cliente (ForeignKey Cliente)
    * Vendedor responsável (ForeignKey Vendedor)
    * Tipo de Materia prima
        -> Esquadria de aluminio
        -> Vidro temperado
    * Cor do Alumínio
        -> Branco
        -> Preto
        -> ...
    * Produto
    """

    MATERIA_PRIMA = (
        ('esquadria', 'Esquadria de Alumínio'),
        ('temperado', 'Vidro Temperado'),
                    )

    COR_DO_ALUMINIO = (
        ('BR', 'Pintura Branco'),
        ('PT', 'Pintura Preto'),
        ('BZ', 'Anodizado Bronze'),
        ('FC', 'Anodizado Fosco'),
        ('AM', 'Pintura Amadeirado'),
                    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    materia_prima = models.CharField(max_length=10, choices=MATERIA_PRIMA,)
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)
    pintura = models.CharField(max_length=50, choices=COR_DO_ALUMINIO)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nome

