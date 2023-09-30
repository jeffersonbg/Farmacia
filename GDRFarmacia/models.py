from django.db import models

# Create your models here.

# endereco_model.py

from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    referencia = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rua}, {self.numero_casa} - {self.bairro}, {self.cidade}/{self.estado}, CEP: {self.cep}"
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
