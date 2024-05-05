# Exercício Python 107: Crie um módulo 
# chamado moeda.py que tenha as funções   
# incorporadas aumentar(), diminuir(), dobro() e 
# metade(). Faça também um programa que 
# importe esse módulo e use algumas dessas 
# funções.
import moeda

price = float(input('Enter the price: R$'))
print(f'The half of R${price} is R${moeda.metade(price)}')
print(f'The double of R${price} is R${moeda.dobro(price)}')
print(f'Increasing 10%, we have R${moeda.aumentar(price, 10)}')
