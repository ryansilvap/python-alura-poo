from classes.Avaliacao import Avaliacao
from classes.cardapio.ItemCardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria}'

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Avaliação: {restaurante.media_das_notas} | Status: {restaurante.ativo}')

    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        avaliacao._nota = 5 if nota > 5 else nota
        self._avaliacao.append(avaliacao)

    @property
    def media_das_notas(self):
        if not self._avaliacao:
            return f'Ainda não há avaliação para o restaurante {self.nome}'

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return str(media)

    def adicionar_ao_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
