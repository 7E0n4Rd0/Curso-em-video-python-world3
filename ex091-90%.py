# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random, time, operator
players = {}
counter = 1
for index in range(1, 5):
    players[f'Player {index}'] = random.randint(1, 6)
for keys, value in players.items():
    print(f'>>> The {keys} rolled the dice and got the number {value}')
    time.sleep(2)
print('-='*30)
time.sleep(2)
players = sorted(players.items(), key=operator.itemgetter(1), reverse=True) # I didn't knew about this method sorted() and 
print('    Ranking\n','-='*30) # I could searched about it before.
for index, value in enumerate(players):
	print(f'	{index+1}° place is {value[0]} with the number {value[1]}.')
	time.sleep(1)
print('-='*30)
