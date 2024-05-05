# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
value = list()
while True:
    value.append(int(input('Enter some number: ')))
    for c in value:
        if value.count(c) >= 2:
            value.pop()
            print(f"I'll not put this number in the List!")
    # I used a loop to do this part, I could use this:
    """if c not in value:
            value.append(c)
       else:
            print(f'This number is duplicated')"""
    answer = str(input('Do you want to continue? '))
    while answer not in 'YyNn':
        answer = str(input('ERROR! Do you want to continue? '))
    if answer in 'Nn':
        break
print(f'-=-'*20)
print(f'The numbers you typed was: {value}')
print(f'-=-'*20)