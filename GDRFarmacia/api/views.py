"""Views"""
from rest_framework.viewsets import ModelViewSet
from GDRFarmacia.models import Endereco
from GDRFarmacia.api.serializers import EnderecoSerializer
from GDRFarmacia.models import Usuario
from GDRFarmacia.api.serializers import UsuarioSerializer
from GDRFarmacia.models import Funcionario
from GDRFarmacia.api.serializers import FuncionarioSerializer
from GDRFarmacia.models import Cliente
from GDRFarmacia.api.serializers import ClienteSerializer
from GDRFarmacia.models import Produto
from GDRFarmacia.api.serializers import ProdutoSerializer
from GDRFarmacia.models import Estoque
from GDRFarmacia.api.serializers import EstoqueSerializer


class EnderecoListCreateView(ModelViewSet):
    """Endereço """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class UsuarioListCreateView(ModelViewSet):
    """Usuario"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class FuncionarioListCreateView(ModelViewSet):
    """Funcionario"""
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class ClienteListCreateView(ModelViewSet):
    """Cliente"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutoListCreateView(ModelViewSet):
    """Produto"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class EstoqueListCreateView(ModelViewSet):
    """Estoque"""
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
