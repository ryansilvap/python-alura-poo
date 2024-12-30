from classes.cardapio.ItemCardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self):
        return f'Nome: {self._nome} | Preço: {self._preco} | Tipo: {self._tipo} | Tamanho: {self._tamanho} | Descrição: {self._descricao}'

    def aplicar_desconto(self):
        pass
