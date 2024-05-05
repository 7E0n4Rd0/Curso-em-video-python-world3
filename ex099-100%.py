# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
import time

def maior(*number):
    print('Analysing this values...')
    if(len(number) == 0):
        print(f'Were typed {len(number)} values.')
        print(f'The highest value was {len(number)}')
    else:
        for value in range(0, len(number)):
            print(number[value], end=' ',flush=True)
            time.sleep(0.5)
            if(value == 0):
                higher = number[value]
            elif(number[value] > higher):
                higher = number[value]
        print('Were typed','values.' if len(number)>1 else 'value.')
        print(f'The highest value was {higher}')
        print('-='*30)
        time.sleep(1)

# Main code
maior(8, 9, 6, 10, 35, 0)
maior(4, 5, 9)
maior(3, 7)
maior(6)
maior()
