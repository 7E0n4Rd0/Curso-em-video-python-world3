# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
# até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Desafio extra: Adicionar a pergunta se quer continuar e continuar o programa.
numbers_extensive = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                     'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
                     'Twenty')
while True:
    number = int(input('Enter some number (Between 0 and 20): '))
    while number < 0 or number > 20:
        print('Error!!', end=' ')
        number = int(input('Enter some number (Between 0 and 20): '))
    for c in range(0, len(numbers_extensive)):
        if c == number:
            print(f'You typed the number \033[32m{numbers_extensive[c]}\033[m.')
    answer = str(input('Do you want to continue? [Y/N] ')).strip()[0]
    while answer not in 'YyNn':
        print('Error!!', end=' ')
        answer = str(input('Do you want to continue? [Y/N] ')).strip()[0]
    if answer in 'Nn':
        print('Bye Bye')
        break
    else:
        print('-=-'*20)
