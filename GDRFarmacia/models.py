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

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    precoVenda = models.DecimalField(max_digits=10, decimal_places=2)
    precoCompra = models.DecimalField(max_digits=10, decimal_places=2)
    quantidadeEmEstoque = models.PositiveIntegerField()
    fabricante = models.CharField(max_length=255)
    fornecedor = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    def cadastrarProduto(self, nome, descricao, categoria, precoVenda, precoCompra, quantidadeEmEstoque, fabricante, fornecedor):
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.precoVenda = precoVenda
        self.precoCompra = precoCompra
        self.quantidadeEmEstoque = quantidadeEmEstoque
        self.fabricante = fabricante
        self.fornecedor = fornecedor
        self.save()

    def imprimir(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço de Venda: R${self.precoVenda:.2f}")
        print(f"Preço de Compra: R${self.precoCompra:.2f}")
        print(f"Quantidade em Estoque: {self.quantidadeEmEstoque}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Fornecedor: {self.fornecedor}")

class Estoque(models.Model):
    quantidadeMinima = models.IntegerField()
    produtoList = models.ManyToManyField(Produto, related_name='estoque')

    def adicionarProduto(self, produto):
        if isinstance(produto, Produto):
            self.produtoList.append(produto)
        else:
            print("O objeto não é um Produto e não pode ser adicionado ao estoque.")

    def removerProduto(self, produto):
        if produto in self.produtoList:
            self.produtoList.remove(produto)
        else:
            print("Produto não encontrado no estoque.")

    def listarProdutos(self):
        for produto in self.produtoList:
            produto.imprimir()

    def notificarEstoqueBaixo(self):
        for produto in self.produtoList:
            if produto.quantidadeEmEstoque < self.quantidadeMinima:
                print(f"Notificação: O produto {produto.nome} está com a quantidade abaixo do mínimo. Quantidade atual: {produto.quantidadeEmEstoque}")

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigoVenda = models.CharField(max_length=100)
    listProduto = models.ManyToManyField(Produto)
    dataCompra = models.DateField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    formaPagamento = models.CharField(max_length=50)
    nomeFuncionario = models.CharField(max_length=100)

    def calcularValorTotal(self):
        total = sum(produto.precoVenda for produto in self.listProduto.all())
        return total

    def adicionarProduto(self, produto):
        self.listProduto.add(produto)

    def Imprimir(self):
        print(f"Código da Venda: {self.codigoVenda}")
        print(f"Cliente: {self.cliente.nome}")
        print("Produtos:")
        for produto in self.listProduto.all():
            print(f"  - {produto.nome}: R${produto.precoVenda}")
        print(f"Data da Compra: {self.dataCompra}")
        print(f"Desconto: R${self.desconto}")
        print(f"Forma de Pagamento: {self.formaPagamento}")
        print(f"Funcionário: {self.nomeFuncionario}")
        print(f"Valor Total: R${self.calcularValorTotal()}")

class Caixa(models.Model):
    def __init__(self):
        self.historicoVenda = []
        self.historicoDevolucoes = []

    def validarVenda(self, compra):
        # Verifica se a compra é válida antes de adicioná-la ao histórico
        if isinstance(compra, Compra):
            self.historicoVenda.append(compra)
            print(f"Compra validada e registrada. Código da Venda: {compra.codigoVenda}")
        else:
            print("Erro: Compra inválida. A venda não foi registrada.")

    def encontrarVenda(self, codigo):
        # Encontra uma venda no histórico pelo código da venda
        for compra in self.historicoVenda:
            if compra.codigoVenda == codigo:
                return compra
        return None

    def processarDevolucao(self, codigoVenda, produtos_devolvidos):
        compra = self.encontrarVenda(codigoVenda)
        if compra:
            for produto_devolvido in produtos_devolvidos:
                if isinstance(produto_devolvido, Produto):
                    if produto_devolvido in compra.listProduto.all():
                        compra.listProduto.remove(produto_devolvido)
                        produto_devolvido.quantidadeEmEstoque += 1
                        produto_devolvido.save()
                        print(f"Produto {produto_devolvido.nome} devolvido e adicionado ao estoque.")
                    else:
                        print(f"Erro: Produto {produto_devolvido.nome} não pertence à compra.")
                else:
                    print("Erro: Produto inválido.")
            self.historicoDevolucoes.append({"codigoVenda": codigoVenda, "produtos_devolvidos": produtos_devolvidos})
        else:
            print(f"Erro: Venda com código {codigoVenda} não encontrada.")

    def historicoDevolucoes(self):
        return self.historicoDevolucoes