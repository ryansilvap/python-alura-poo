
#5. Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

#6. Implemente o Metodo Especial str na Classe Filha (Moto): Adicione um metodo especial str à classe Moto que estenda o metodo da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Tipo: {self._tipo} | Estado: {self._ligado}'