# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
number = tuple(randint(0, 10) for c in range(0, 5))
# Or "number = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))", literally I used the
# hard way 💀. - 05/20/2023 - 11:42
print('-=-'*20)
print(f'The drawn numbers are: {number}.')
print(f'The lowest number is: {min(number)}')
print(f'The highest number is {max(number)}')
print('-=-'*20)
