# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de 
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(message=''):
    while True:
        try:
            number = int(input(message))
        except (ValueError, TypeError):
            print('\033[31mError!! Enter only integer numbers\033[m')
        except Exception as error:
            print(f'The problem was caused by: {error.__class__}')
        except KeyboardInterrupt:
            print('\n\033[31mThe user choosed to not inform the Integer number.\033[m')
            number = 0
            break
        else:
            break
    return number


def leiaFloat(message=''):
    while True:
        try:
            number = float(input(message))
        except ValueError:
            print('\033[31mError!! Enter only float numbers\033[m')
        except Exception as error:
            print(f'The problem was caused by: {error.__class__}')
        except KeyboardInterrupt:
            print('\n\033[31mThe user choosed to not inform the Float number.\033[m')
            number = 0.0
            break
        else:
            break
    return number


x = leiaInt('Enter a Integer number: ')
y = leiaFloat('Enter a Float number: ')
print(f'The integer number is {x} and the float number is {y}.')
