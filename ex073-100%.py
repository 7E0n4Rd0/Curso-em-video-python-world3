# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
teams = ('EC Vitória', 'Criciúma', 'Atlético-GO', 'Guarani', 'Botafogo SP', 'Vila Nova', 'Mirassol', 'Chapecoense',
         'Sport Recife', 'Novorizontino', 'Ituano', 'Londrina', 'Ceará SC', 'Avaí', 'CRB', 'Sampaio Corrêa',
         'Ponte Preta', 'Tombense', 'Juventude', 'ABC')
cont = 0
print('-=-'*20)
print('TABELA DO BRASILEIRÃO')
print(teams)
print('-=-'*20)
print('~'*60)
print('The first five teams are: ', end='')
while True:
    if cont <= 4:
        print(teams[cont], end='')
        print(',' if cont != 4 else '.', end=' ')
        cont += 1
    else:
        break
print(f"\n{'~'*60}")
print('The last four teams are: ', end='')
for cont in range(0, len(teams)):
    if cont >= 16:
        print(teams[cont], end='')
        print(',' if cont != 19 else '.', end=' ')
print(f'\n{"~"*60}')
print('The teams in Alphabetic order are: ', end='')
print(sorted(teams))
print('~'*60)
print('The position of the team Chapecoense is: ', end='')
cont = 0
for cont in range(0, len(teams)):
    find = teams[cont].find('Chapecoense')
    if find != -1:
        print(f'{cont+1}°')
print('~'*60)
# I could use the "Fatiamento" to do this exercise. 05/19/2023 - 21:10
