# 5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from Livro import Livro

# ____
livro = Livro('Ponto de Inflexão', 'Flávio Augusto', 2020)
livro1 = Livro('Ultralearning', 'Scott', 2020)

# 6. No arquivo biblioteca.py, empreste o livro chamando o metodo emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro.emprestar()
print(f'Status do livro {livro.titulo}: {livro.disponivel}')

# 6. No arquivo biblioteca.py, utilize o metodo estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
print(Livro.verificar_disponibilidade(2020))