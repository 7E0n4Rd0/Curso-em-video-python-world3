"""num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')"""
"""valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao final da lista.')"""
a = [2, 3, 4, 7]
# b = a  Aqui ele vai fazer um ligamento entre as Listas A e B, qualquer alteração irá afetar em ambas.
b = a[:]  # Aqui ele vai criar uma cópia de todos os elementos de A e colocar em B usando o Fatiamento.
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')
