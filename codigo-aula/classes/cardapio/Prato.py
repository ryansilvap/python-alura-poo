from classes.cardapio.ItemCardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        #desconto de 5%
        self._preco *= 0.95