# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.

import moeda

price = float(input('Enter the price: R$'))
print(f'The half of {moeda.moeda(price)} is {moeda.moeda(moeda.metade(price))}')
print(f'The double of {moeda.moeda(price)} is {moeda.moeda(moeda.dobro(price))}')
print(f'Increasing 10%, we have {moeda.moeda(moeda.aumentar(price, 10))}')

