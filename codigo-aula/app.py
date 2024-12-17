from classes.Restaurante import Restaurante
from classes.cardapio.Bebida import Bebida
from classes.cardapio.Prato import Prato

restaurante_praca = Restaurante('praça', 'Goumert')
restaurante_pizza = Restaurante('MisterChef', 'pizzaria')
restaurante_japones = Restaurante('Sushi', 'japonesa')

restaurante_pizza.alterar_status()

restaurante_japones.receber_avaliacao('Ryan', 10)
restaurante_japones.receber_avaliacao('John', 7.8)
restaurante_japones.receber_avaliacao('Alice', 4.5)

bebida = Bebida('Suco', 7.5, '500ml')
prato = Prato('Prato', 19.99, 'G')

def main():
    # Restaurante.listar_restaurantes()
    print(bebida)
    print(prato)

if __name__ == '__main__':
    main()
