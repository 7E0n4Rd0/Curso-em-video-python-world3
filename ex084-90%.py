# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# a) Quantas pessoas foram cadastradas;
# b) Uma listagem com as pessoas mais pesadas;
# c) Uma listagem com as pessoas mais leves;

peoples = list()
data = list()
higher = lower = 0
peopleRegistered = 0
while True:
    data.append(str(input("Name: ")))
    data.append(float(input("Weight: ")))
    if peopleRegistered == 0:
        higher = lower = data[1]
    else:
        if data[1] > higher:
            higer = data[1]
        if data[1] < lower:
            lower = data[1]
    peopleRegistered += 1
    answer = str(input("Do you want to continue? [Y/N] ")).strip()
    peoples.append(data[:])
    data.clear()
    if answer in 'Nn':
        break
print('-='*30)
print(f'It was registered {peopleRegistered} peoples.')
print(f'The higher weight was {higher}Kg. Weight of ',end='')
for people in peoples:
    if people[1] == higher:
        print(f'[{people[0]}]', end='')
print()
print(f'The lower weight was {lower}Kg. Weight of ', end='')
for people in peoples:
    if people[1] == lower:
        print(f'[{people[0]}]', end='')
print()
# I changed a few lines of code, just to be like the teacher's answer.