from rest_framework.viewsets import ModelViewSet
from GDRFarmacia.models import Endereco
from GDRFarmacia.api.serializers import EnderecoSerializer
from GDRFarmacia.models import Usuario
from GDRFarmacia.api.serializers import UsuarioSerializer
from GDRFarmacia.models import Funcionario
from GDRFarmacia.api.serializers import FuncionarioSerializer
from GDRFarmacia.models import Cliente
from GDRFarmacia.api.serializers import ClienteSerializer

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