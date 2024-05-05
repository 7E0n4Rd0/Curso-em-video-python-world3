# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random, time;
gamenumbers = []
numberbefore = 0
print('====== Mega Sena ======')
games = int(input('How much games do you want to generate? '))
for i in range(0, games):
    gamenumbers.append([]) # Here it adds a list according to the number of 'games' the user wants.
    for j in range(0, 6):
        randomnumber = int(random.randint(1, 60))
        if randomnumber not in gamenumbers[i]:
            numberbefore = randomnumber
            gamenumbers[i].insert(i, randomnumber) # Here it adds a random number in 'gamenumbers[i]' which means, 'insert the number in the list in position i'.          
        elif numberbefore in gamenumbers[i]:
            while True:
                randomnumber = int(random.randint(1, 60))
                if numberbefore != randomnumber:
                    numberbefore = randomnumber
                    gamenumbers[i].insert(i, randomnumber)
                    break
    gamenumbers[i].sort()
for i in range(0, games):
    print(f'Combination {i+1}: {gamenumbers[i]} ')
    time.sleep(1)
print('{:=^25}'.format(' Good Luck '))
