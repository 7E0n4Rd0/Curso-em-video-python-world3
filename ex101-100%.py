# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como 
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
import datetime

def voto(year_born):
    age = int(datetime.date.today().year - year_born)
    if(age < 18):
        print(f'NEGADO. Você tem {age} anos.')
    elif(age >= 18 and age < 65):
        print(f'OBRIGATÓRIO. Você tem {age} anos.')
    else:
        print(f'OPCIONAL. Você tem {age} anos')

# Main code

year_born = int(input('Enter your birth year: '))
voto(year_born)