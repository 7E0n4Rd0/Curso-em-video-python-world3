# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
# mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
number = tuple(n := int(input('Enter some number: ')) for c in range(0, 4))
print(f'You typed the numbers {number}')
print(f'The pair numbers are: ', end='')
for c in range(0, 4):
    # if number[c] == 9:
    #    nine += 1
    if number[c] % 2 == 0:
        print(f'{number[c]}', end=' ')
if 3 in number:  # I forget the method ".index()" return an error if there isn't a number in the Tuple. 05/20/2023
    # - 13:07
    print(f'\nThe position of the first number 3 is: {number.index(3) + 1}° position')
else:
    print(f'\nThe number 3 was not typed.')
# print(f'Showed {nine} time(s) the number 9.')
print(f'The number 9 showed {number.count(9)} times')  # I could use the method ".count" instead of "if number[c] == 9"
# 05/20/2023 - 13:01
