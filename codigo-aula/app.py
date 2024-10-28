from classes.Restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Goumert')
restaurante_pizza = Restaurante('MisterChef', 'pizzaria')
restaurante_japones = Restaurante('Sushi', 'japonesa')

restaurante_pizza.alterar_status()

restaurante_japones.receber_avaliacao('Ryan', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
