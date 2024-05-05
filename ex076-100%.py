# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
# sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-' * 40)
print(f'{"Shopping List":^35}')
print('-' * 40)
products = ('Pencil', 1.75, 'Eraser', 2.00, 'Notebook', 15.90, 'Case', 25.00, 'Protractor', 4.20, 'Compass', 9.99,
            'Backpack', 120.32, 'Pens', 22.30, 'Book', 34.90)
# print(f'{products[0]:.<25}R${products[1]: >9}') Example what I need to do for all of them. - 05/21/2023 - 19:42
a = 0
b = -17
while True:  # Neste trecho do código esta dando um erro do range estar fora da tupla, amanhã eu resolvo. - 05/21/2023 -
    # 20:49
    print(f'{products[a]:.<25}', end='')
    print(f'R${products[b]: >10.2f}')
    if a == 16 and b == -1:
        a += 1
        b += 1
        break
    else:
        a += 2
        b += 2
# or
"""for c in range(0, len(products)):
    if c % 2 == 0:
	    print(f'{products[c]:.<25}', end='')
    else:
	    print(f'R${products[c]: >10.2f}')"""
print('-' * 40)
# Done, I fixed the cod. When the variables are equal 16 and b equal -1, I just put '+=' 1, because if I put 2, will
# get a range error. - 05/22/2023 - 05:47
