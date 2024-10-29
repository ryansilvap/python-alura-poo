# 1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    # 2. Na classe Livro, adicione um metodo especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'O livro {self._titulo} do autor {self._autor} publicado em {self._ano_publicacao}'

    # ____
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @property
    def is_disponivel(self):
        return self._disponivel

    # 3. Adicione um metodo de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o metodo emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self._disponivel = False

    @property
    def disponivel(self):
        return '✅' if self._disponivel else '❌'

    # 4. Adicione um metodo estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        return [livro.titulo for livro in Livro.livros if livro._ano_publicacao == ano and livro.is_disponivel]
