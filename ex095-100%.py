# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

import time
soccerplayer = {}
soccerplayer_list = []
gols = list()
allgols = 0
while True:
    soccerplayer['name'] = str(input('Name: ')).strip().capitalize()
    games = int(input(f'How many games {soccerplayer["name"]} played? '))
    for i in range(0, games):
        gols.append(int(input(f'How many gols {soccerplayer["name"]} did in game {i+1}? ')))
        soccerplayer['gols'] = gols[:]
        allgols += gols[i]
    soccerplayer['total'] = allgols
    soccerplayer_list.append(soccerplayer.copy())
    soccerplayer.clear()
    gols.clear()
    allgols = games = 0
    answer = str(input('Do you want to continue? [Y/N] ')).strip().capitalize()
    while answer not in 'YyNn':
        print('Error, please enter only Y or N')
        answer = str(input('Do you want to continue? [Y/N] ')).strip().capitalize()
    if answer in 'Nn':
        break
    print('=+'*20)
print('-='*30)
print(soccerplayer_list) # Now I have to make a spreadsheet with the data.
print(f'{"N°":<10} {"Name":^10} {"Total of Gols":>10}')
print('--'*25)
for i in range(0, len(soccerplayer_list)):
    print(f'{i:<10}', end=' ')
    for key, value in soccerplayer_list[i].items():
        if key in 'name':
            print(f'{soccerplayer_list[i]["name"]:^10}', end=' ')
        elif key in 'total':
            print(f'{soccerplayer_list[i]["total"]:>7}', end=' ')
    print()
print('--'*25)
while True:
    answer = int(input('Enter a player number to expands the soccer player info [Type -1 to exit] '))
    if answer == -1:
        break
    for i in range(0, len(soccerplayer_list)):
        if answer == i:
            print('<=>'*20)
            for key, value in soccerplayer_list[i].items():
                if key in 'name':
                    print(f' The {key} of the soccer player is {value} and played {len(soccerplayer_list[i]["gols"])} games:')
                elif key not in 'gols':
                    print(f'  The {key} of gols is {value}.')
                else:
                    for index, v in enumerate(value):
                        print(f'>>>> In the game {index+1}, {soccerplayer_list[i]["name"]} made {v} gol(s).') # This lists all the data.
            print('<=>'*20)
        elif answer > len(soccerplayer_list)-1:
            print('This value is out of the range.')
time.sleep(1)
print('Bye bye')