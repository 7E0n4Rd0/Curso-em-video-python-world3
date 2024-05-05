from functions import *
from time import sleep

def line(simbol='-',size=30):
    print(simbol*size)

def heading(msg='',size=30):
    line('~',size)
    print(msg.center(size))
    line('~',size)

def main_menu():
    while True:
        heading('Menu',50)
        print('\033[32m1 - Register person\033[m\n\033[34m2 - Consult list of people\033[m\n\033[31m3 - Exit\033[m')
        answer = readInt('>>> ')
        if answer == 1:
            heading('Option 1: Register person',50)
            try:
                file = open('pythonexercícios_W03/ex115/data.txt', "x")
            except FileExistsError:
                file = open('pythonexercícios_W03/ex115/data.txt',"a+")
            except Exception as error:
                print('O error foi ocorrido por ',error.__class__)
            sleep(2)
            registerPerson()
            file.close()
        elif answer == 2:
            heading('Option 2: Consult list of people',50)
            sleep(2)
            queryData('pythonexercícios_W03/ex115/data.txt')
        elif answer == 3 or answer == 0:
            break
        else:
            print('\033[31mThis option does not exists!!\033[m')
    print('Bye Bye')