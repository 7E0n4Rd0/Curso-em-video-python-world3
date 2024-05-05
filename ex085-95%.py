# Crie um programa onde o usuário vai digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numbers = [[],[]]
for index in range(0, 7):
    number = int(input(f'Type the {index+1}° number: '))
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)
numbers[0].sort()
numbers[1].sort()
print('<=>'*30)
print(f'The pair numbers are: {numbers[0]}')
print(f'The unpair numbers are: {numbers[1]}')
