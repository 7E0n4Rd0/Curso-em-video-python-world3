# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

price = float(input('Enter the price: R$'))
print(f'The half of {moeda.moeda(price)} is {moeda.metade(price, True)}')
print(f'The double of {moeda.moeda(price)} is {(moeda.dobro(price, True))}')
print(f'Increasing 10%, we have {moeda.aumentar(price, 10, True)}')
print(f'Reducing 13%, we have {moeda.diminuir(price, 13, True)}')