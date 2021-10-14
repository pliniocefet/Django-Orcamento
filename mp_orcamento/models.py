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
    nome = models.CharField(max_length=128)  # nome vendedor
    telefone = models.CharField(max_length=30)  # telefone vendedor

    objects = models.Manager()

    def __str__(self):
        return self.nome



# MODELS PARA LINHA DE PRODUTOS
class Linha(models.Model):
    codigo = models.CharField(max_length=64)  # codigo
    descricao = models.CharField(max_length=256)  # descrição

    objects = models.Manager()

    def __str__(self):
        return self.codigo
    
    def __unicode__(self):
        return self.codigo


class Aluminio(models.Model):
    codigo = models.CharField(max_length=64)  # codigo
    descricao = models.CharField(max_length=256)  # descricao
    peso = models.FloatField()  # peso
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)  # linha

    objects = models.Manager()
    
    def __str__(self):
        return self.descricao
    
    def __unicode__(self):
        return self.descricao


class Acessorio(models.Model):
    codigo = models.CharField(max_length=64)  # codigo
    descricao = models.CharField(max_length=256)  # descricao
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)  # linha
    preco = models.FloatField()  # preço

    objects = models.Manager()
    
    def __str__(self):
        return self.descricao

    def __unicode__(self):
        return self.descricao


class Vidro(models.Model):
    codigo = models.CharField(max_length=64)  # codigo
    descricao = models.CharField(max_length=256)  # descricao
    preco = models.FloatField()  # preço

    objects = models.Manager()

    def __str__(self):
        return self.descricao

    def __unicode__(self):
        return self.descricao


class Produto(models.Model):
    codigo = models.CharField(max_length=64)  # codigo
    descricao = models.CharField(max_length=256)  # descrição
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)  # vincular linha
    vidro = models.ForeignKey(Vidro, on_delete=models.CASCADE)  # vincular vidro
    aluminio = models.ForeignKey(Aluminio, on_delete=models.CASCADE)  # vincular aluminio
    acessorio = models.ForeignKey(Acessorio, on_delete=models.CASCADE)  # vincular acessorio
      
    def __str__(self):
        return self.descricao

    def __unicode__(self):
        return self.descricao


# MODELS PARA ORÇAMENTOS
class Orcamento(models.Model):
    """
    ITENS DO MODEL ORÇAMENTO
    * Nome do Cliente (ForeignKey Cliente)
    * Telefone do Cliente (ForeignKey Cliente)
    * Endereço do Cliente (ForeignKey Cliente)
    
    * Vendedor responsável (ForeignKey Vendedor)
        RELACIONAMENTO ORÇAMENTO X VENDEDOR
        -- Orçamento só pode ter um único vendedor mas vendedor pode ter vários orçamentos
        -- Relacionamento Many To One

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
    pintura = models.CharField(max_length=50, choices=COR_DO_ALUMINIO)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nome

