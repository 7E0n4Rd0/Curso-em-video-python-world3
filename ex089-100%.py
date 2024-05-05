# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e que permita o usuário possa mostrar as notas de cada aluno individualmente.

import time

data = list()
grade01 = grade02 = 0
summedium = float()
while True:
        name = str(input('Name: '))
        grade01 = float(input('Grade 01: '))
        grade02 = float(input('Grade 02: '))
        data.append([name, float(grade01), float(grade02)])
        answer = str(input('Do you want to continue? [Y/N] '))
        if answer in 'Nn':
            break 
print('<->'*15)
print('{:<10} {:^10} {:>10} '.format('N°', 'Name', 'Medium'))
print('-='*20)
for i in range(0, len(data)):
    print(f'{i:<10}', end=' ')
    print(f'{data[i][0]:^10}', end=' ')
    for j in range(1, len(data[i])):
        summedium += data[i][j]
    media = (summedium)/2
    print(f'{media:>9.2f}', end=' ')
    summedium -= summedium
    media -= media
    print()
while True: 
    answer = int(input("Type a number of the student to show her/his grade [Type -1 to finish the programm]: "))
    if answer == - 1:
        break
    for i in range(0, len(data)):
        if answer == i:
            print('-='*30)
            print(f'The grades of {data[i][0]} are {data[i][1]} and {data[i][2]}')
            print('-='*30)
time.sleep(1)
print('Bye Bye')
