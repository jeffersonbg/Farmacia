from django.db import models

# Create your models here.

# endereco_model.py



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

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")

    # Classe Funcionario herda de Usuario
class Funcionario(Usuario):
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}"

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: {self.salario}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")

    @classmethod
    def cadastrar_funcionario(cls, nome, email, senha, cargo, salario, telefone, cpf):
        funcionario = cls(
            nome=nome,
            email=email,
            senha=senha,
            cargo=cargo,
            salario=salario,
            telefone=telefone,
            cpf=cpf
        )
        funcionario.save()
        return funcionario

    def atualizar_funcionario(self, nome, email, senha, cargo, salario, telefone, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
        self.telefone = telefone
        self.cpf = cpf
        self.save()

class Cliente(Usuario):
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"Cliente: {self.nome}"

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")

    @classmethod
    def cadastrar_cliente(cls, nome, email, senha, telefone, cpf):
        cliente = cls(
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            cpf=cpf
        )
        cliente.save()
        return cliente

    def atualizar_cliente(self, nome, email, senha, telefone, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.cpf = cpf
        self.save()