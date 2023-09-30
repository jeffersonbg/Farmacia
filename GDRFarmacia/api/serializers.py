"""Serializers"""
from rest_framework import serializers
from GDRFarmacia.models import Endereco
from GDRFarmacia.models import Usuario


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
