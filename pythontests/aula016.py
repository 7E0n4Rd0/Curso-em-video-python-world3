# "Tuplas são Imutáveis"

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)  # <- Print normal, apresentando parênteses e virgulas.
# -=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Printar sem os parênteses e vírgulas:

for cont in range(0, len(lanche)):  # <- Este usa o range e o len da variável composta para mostrar o valor dentro da
    print(f'Eu vou comer {lanche[cont]}')  # posição.

for comida in lanche:  # <- Este usa diretamente a variável composta atribuindo o valor da posição para a variavel de
    print(f'Eu vou comer {comida}')  # controle.
# -=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Mostrando a posição:

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
print('Comi pa caramba')
# -=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print(sorted(lanche))  # <- O sorted() ele organiza a tupla, mas ele não altera a configuração dela.
# -=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
a = (2, 5, 4)  # Quando as Tuplas são números e você pode criar uma variável para somar, ele vai juntar elas e vai ser
b = (5, 8, 1, 2)  # de acordo com a ordem; se for a + b vai mostrar: (2, 5, 4, 5, 8, 1, 2) e se for b + a vai mostrar:
c = b + a  # (5, 8, 1, 2, 2, 5, 4).
print(c)
print(c.index(5, 1))
# O .index() mostra a posição de um número de acordo com a 1° ocorrência; se fosse para mostrar o número 2 (Em relação
# ao valor de c sendo b + a) ele vai mostrar o resultado na posição 3, mas tem um outro "2" na posição 4. Para mostrar
# ele teria de colocar ".index(2, 4)" para pular o número 2 da posição 3 contar a partir do indíce 4, logo mostrando o
# número 2 da posição 4.
# -=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Adicionando valores de tipos diferentes dentro das Tuplas.
pessoa = ('Gustavo', 39, 'M', 39.88)
print(pessoa)
# Como foi dito as Tuplas são imutáveis, mas é possível APAGAR TODOS OS VALORES DELA usando o comando del()
del pessoa
# Mesmo assim, não é possível deletar um valor dentro da Tupla; se digitar por exemplo: del pessoa[0] ele vai retornar
# com um erro.
# -=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
