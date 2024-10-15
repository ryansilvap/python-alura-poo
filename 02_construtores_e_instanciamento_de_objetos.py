# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}'

primeiro_carro = Carro('Fiesta', 'Prata', '2013')
print(primeiro_carro)

# 2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos. Utilize o metodo especial __str__.

class Restaurante:
    def __init__(self, nome, categoria, nota, tipo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.nota = nota
        self.tipo = tipo

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Status: {self.ativo} | Nota: {self.nota} | Tipo: {self.tipo}'

restaurante_praca = Restaurante('Praça', 'Italiano', 9.5, 'Delivery')
# restaurante_pizza = Restaurante('Pizza', 'Italiano', 10, 'Presencial & Delivery')

print(restaurante_praca)
# print(restaurante_pizza)

