from classes.cardapio.ItemCardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        #desconto de 8%
        self._preco *= 0.92