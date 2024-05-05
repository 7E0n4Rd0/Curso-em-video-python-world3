"""def lin(): #Criar linha
    print('-'*30)"""


"""def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


título("Curso em Vídeo")
título("Aprenda Python")
título("Gustavo Guanabara")"""
# Momento prática da aula
"""def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)"""

"""def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end=' ')
    print('Fim!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)"""

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)