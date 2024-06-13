from peewee import *

db = SqliteDatabase('Vendas.db')

class BaseModel(Model):
    class Meta:
        database = db

class Pedido(Model):
    datadopedido = CharField()
    enderecoentrega = CharField()
    observacao = CharField()
    class Meta:
        database = db

class Clientes(Model):
    nome = CharField()
    cpf = DecimalField()
    email= CharField()
    telefone = DecimalField()
    Endereco = CharField()
    class Meta:
        database = db

class Fornecedor(Model):
    nome = CharField()
    cnpj = DecimalField()
    email= CharField()
    telefone = DecimalField()
    endereco = CharField()
    class Meta:
        database = db

class Produto(Model):
    quantidade_estoque = DecimalField()
    valor_unitario = DecimalField()
    nome = CharField()
    class Meta:
        database = db

class MercadoriaComprada(Model):
    quantidade_comprada = DecimalField()
    valor_compra = DecimalField()
    class Meta:
        database = db

class Compra(Model):
    data_compra = CharField()
    class Meta:
        database = db
