# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.
values = list()
for counter in range(0, 5):
    values.append(int(input(f'Enter some number for the position {counter}: ')))
print('-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'You typed: {values}')
lowest_number = higher_number = 0
for position, counter in enumerate(values):
    if position == 0:
        lowest_number = counter
        higher_number = counter
    if counter < lowest_number:
        lowest_number = counter
    elif counter > higher_number:
        higher_number = counter
print(f'The lowest number is {lowest_number} in positions ', end='')
for position, counter in enumerate(values):
    if lowest_number == counter:
        print(f'{position}...', end=' ')
print(f'\nThe highest number is {higher_number} in positions ', end='')
for position, counter in enumerate(values):
    if higher_number == counter:
        print(f'{position}...', end=' ')
