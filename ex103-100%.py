# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros 
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do  
# jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(name='<unknown>', gols='0'):
	print('-'*30)
	print(f'soccer player {name} did {gols} gols.')

	
name = str(input('Enter the soccer player name: ')).capitalize().strip()
gols = str(input('How many gols she / he did? '))

if(name != '' and gols != '' and gols.isnumeric()): # Name: Ok and Gols: Ok
	ficha(name, gols)
if(name != '' and gols == '' or not gols.isnumeric()): # Name: Ok and Gols: none
	ficha(name=name)
if(name == '' and gols != '' and gols.isnumeric()): # Name: none and Gols: Ok 
	ficha(gols=gols)
if(name == '' and gols == ''): # Name: none and Gols: none
	ficha()
