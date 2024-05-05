# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois, vai ler a quantidade de gols feitos em cada parida. No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante
# o campeonato.

soccerplayer = {}
gols = list()
allgols = 0
soccerplayer['name'] = str(input('Name: ')).strip().capitalize()
games = int(input(f'How many games {soccerplayer["name"]} played? '))
for i in range(0, games):
	gols.append(int(input(f'	How many gols {soccerplayer["name"]} did in game {i+1}? ')))
	soccerplayer['gols'] = gols[:]
	allgols += gols[i]
soccerplayer['total'] = allgols
print(soccerplayer)
print('-='*30)
for key, value in soccerplayer.items():
	if key in 'name':
		print(f' The {key} of the soccer player is {value} and played {games} games:')
	elif key not in 'gols':
		print(f'  The {key} of gols is {value}.')
	else:
		for index, v in enumerate(value):
			print(f'>>>> In the game {index+1}, {soccerplayer["name"]} made {v} gol(s).')
print('-='*30)
