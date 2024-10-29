# 8.Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o metodo str.

from Livro import Livro

livro = Livro('Ponto de Inflexão', 'Flávio Augusto', 2020)
livro1 = Livro('Ultralearning', 'Scott', 2020)
print(livro)
print(livro1)

def main():
    pass

if __name__ == '__main__':
    main()