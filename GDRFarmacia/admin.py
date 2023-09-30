"""Administradores"""
from django.contrib import admin


# Register your models here.

from GDRFarmacia.models import Endereco  # <--- import the model
from GDRFarmacia.models import Usuario

# Register your models here.

admin.site.register(Endereco)  # <--- register the model
admin.site.register(Usuario)
