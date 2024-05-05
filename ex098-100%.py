# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
import time

def contador(start, end, step):
    if(start < end):
        if(step == 0):
            print(f'Counting from {start} to {end} by {1} by {1}')
            time.sleep(1)
            for i in range(start, end+1, 1):
                print(i,end=' ', flush=True); 
                time.sleep(0.5)
            print(' Fim!')
            print('-='*30)
        else:
            print(f'Counting from {start} to {end} by {abs(step)} by {abs(step)}')
            time.sleep(1)
            for i in range(start, end+1, abs(step)):
                print(i,end=' ',flush=True)
                time.sleep(0.5)
            print(' Fim!')
            print('-='*30)
    elif (start > end):
        if(step == 0):
            print(f'Counting from {start} to {end} by {1} by {1}')
            time.sleep(1)
            for i in range(start, end-1, -1):
                print(i,end=' ',flush=True)
                time.sleep(0.5)
            print(' Fim!')
            print('-='*30)
        else:
            print(f'Counting from {start} to {end} by {abs(step)} by {abs(step)}')
            time.sleep(1)
            for i in range(start, end-1, -abs(step)):
                print(i,end=' ',flush=True)
                time.sleep(0.5)
            print(' Fim!')
            print('-='*30)
    if(start == end):
        print(f'There is not a way to counting from {start} to {end}')    

# Main Code
contador(1, 10, 1)
contador(10, 1, 2)
print('Now it is your turn. ')
start = int(input('Start: '))
end = int(input('End: '))
step = int(input('Step: '))
print('-='*30)
contador(start, end, step)
