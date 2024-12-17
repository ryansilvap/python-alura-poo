# 7. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# 8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

from Carro import Carro
from Moto import Moto

carro1 = Carro('Ford', 'Fiesta', 4)
carro2= Carro('Chevrolet', 'Corsa', 4)
carro3 = Carro('VW', 'Gol', 2)

moto1 = Moto('Honda', 'CG160', 'Casual')
moto2 = Moto('Honda', 'Fazer', 'Esportiva')
moto3 = Moto('Honda', 'Titan', 'Casual')

# 9. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o metodo str.

print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)
