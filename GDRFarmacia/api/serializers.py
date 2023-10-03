"""Serializers"""
from rest_framework import serializers
from GDRFarmacia.models import Endereco
from GDRFarmacia.models import Usuario
from GDRFarmacia.models import Funcionario
from GDRFarmacia.models import Cliente
from GDRFarmacia.models import Produto
from GDRFarmacia.models import Estoque

class EnderecoSerializer(serializers.ModelSerializer):
    """Class Endereco"""
    class Meta:
        """Inicio"""
        model = Endereco
        fields = ['rua', 'bairro', 'numero_casa', 'cep',
                  'referencia', 'estado', 'cidade']


class UsuarioSerializer(serializers.ModelSerializer):
    """Class Usuario"""
    class Meta:
        """Inicio"""
        model = Usuario
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'
