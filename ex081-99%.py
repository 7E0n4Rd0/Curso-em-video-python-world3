#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                   
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

number = list()
answer = str('')
#cont = 0
numberFiveFound = False
while(answer in 'Yy'):
    number.append(int(input('Type a number: ')))
    #cont += 1
    answer = str(input('Do you want to continue? [Y/N] ')).strip()
    if(answer in 'Nn'):
        for c in range(0, len(number)):
            if(number[c] == 5):
                numberFiveFound = True
        number.sort(reverse=True)
        break
print(f'All the {len(number)} numbers typed by the user in decreasing: {number}')
if(numberFiveFound):
    print('There is a number 5 in the list!')
else:
    print('There is not a number 5 in the list!')

# I used 'cont' to count the numbers, but it better use 'len(number)' so I changed.