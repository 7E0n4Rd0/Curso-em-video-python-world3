# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares 
# sorteados pela função anterior.

import random, time

numeros = list()
def sorteia(list):
    print(f'Sorting 5 values in the list: ', end='')
    for index in range(0, 5):
        list.append(random.randint(0, 20))
        print(f'{list[index]}', end=' ',flush=True)
        time.sleep(0.3)

def somaPar(list):
    s = 0
    for value in range(0, len(list)):
        if(list[value] % 2 == 0):
            s += list[value]
    print(f'\nThe sum of all evens values are {s}')

# Main code
sorteia(numeros)
somaPar(numeros)
