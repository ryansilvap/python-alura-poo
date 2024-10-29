from classes.Avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
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
        self._avaliacao.append(avaliacao)

    @property
    def media_das_notas(self):
        if not self._avaliacao:
            return 0

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return str(media)
