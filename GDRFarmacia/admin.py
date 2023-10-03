"""Administradores"""
from django.contrib import admin


# Register your models here.

from GDRFarmacia.models import Endereco  # <--- import the model
from GDRFarmacia.models import Usuario
from GDRFarmacia.models import Funcionario
from GDRFarmacia.models import Cliente
from GDRFarmacia.models import Produto



# Register your models here.

admin.site.register(Endereco)  # <--- register the model
admin.site.register(Usuario)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Produto)
