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
from GDRFarmacia.models import Compra
from GDRFarmacia.api.serializers import CompraSerializer
from GDRFarmacia.models import Caixa
from GDRFarmacia.api.serializers import CaixaSerializer

class EnderecoListCreateView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class UsuarioListCreateView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FuncionarioListCreateView(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ClienteListCreateView(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoListCreateView(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class EstoqueListCreateView(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class CompraListCreateView(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CaixaListCreateView(ModelViewSet):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer