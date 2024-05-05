# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a 
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(message):
    while True:
        number = str(input(message))
        if(not number.isnumeric()):
            print('\033[0;31mError, Type only Integer numbers.\033[m')
        else:
            return number
            break


# Main Code
n = leiaInt('Enter a number: ')
print(f'You typed the number {n}')
