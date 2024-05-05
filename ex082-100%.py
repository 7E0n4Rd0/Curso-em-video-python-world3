# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
number = list()

while(True):
    number.append(int(input("Type a number here: ")))
    answer = str(input("Do you want to continue? [Y/N]"))
    if(answer in 'Nn'):
        pair = []
        unpair = []
        for cont in range(0, len(number)):
            if number[cont] % 2 == 0:
                pair.append(number[cont])
            elif number[cont] % 2 == 1:
                unpair.append(number[cont])
        break

print("=-="*30)
print(f'list of all numbers typed by the user: {number}')
print(f'list of all pair numbers: {pair}')
print(f'list of all unpair numbers: {unpair}')
 