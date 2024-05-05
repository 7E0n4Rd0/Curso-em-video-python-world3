# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com formatação correta.

array = [[], [], []]
for i in range(0, 3): # Line
    for j in range(0, 3): # Column
        number = int(input(f'Type a number in position [{i}][{j}]: ' ))
        array[i].append(number) # "This is the way" we do Arrays in Python. The Mandalorian references lol
print('<=>'*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {array[i][j]} ]',end='')
    print()
