from rest_framework.viewsets import ModelViewSet
from GDRFarmacia.models import Endereco
from GDRFarmacia.api.serializers import EnderecoSerializer
from GDRFarmacia.models import Usuario
from GDRFarmacia.api.serializers import UsuarioSerializer

class EnderecoListCreateView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer