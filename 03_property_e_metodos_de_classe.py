#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um metodo especial __str__ para imprimir uma representação em string da pessoa. Implemente também um metodo de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} tenho {self.idade} anos e trabalho como {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            print(f'Olá, você trabalha com {self.profissao}')
        else:
            print('Olá! Tudo bem?')


ryan = Pessoa('Ryan', 23, 'Python Developer')
print(ryan)
ryan.saudacao

# 1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

# 2. Na classe ContaBancaria, adicione um metodo especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo} | Ativo: {self._ativo}'

    # 3. Adicione um metodo de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o metodo de classe e imprima o valor de ativo.

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
        return 'Ativo' if conta._ativo else 'Inativa'

conta1 = ContaBancaria('John', 15000)
print(ContaBancaria.ativar_conta(conta1))

conta2= ContaBancaria('Kelly', 20000)

print(conta1)
print(conta2)

# 4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

# 5. Crie uma instância da classe e imprima o valor da propriedade titular.

conta3 = ContaBancaria('Victor', 10000)
print(conta3.titular)

# 6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do metodo construtor.

class ClienteBanco:
    clientes = []

    def __init__(self, nome, saldo, cpf, telefone):
        self._nome = nome
        self._saldo = saldo
        self._cpf = cpf
        self._telefone = telefone
        self._ativo = False
        ClienteBanco.clientes.append(self)

    def __str__(self):
        return f'Nome: {self._nome}'

    # 7. Crie um metodo de classe para a conta ClienteBanco.
    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes:
            print(cliente._nome)

cliente1 = ClienteBanco('Kelly', 100, '111.111.111-65', '99 99999-9999')
cliente2 = ClienteBanco('Paul', 200, '111.111.111-66', '99 99999-9998')
cliente3 = ClienteBanco('John', 300, '111.111.111-67', '99 99999-9997')

ClienteBanco.listar_clientes()


