# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar. 

import datetime

person = dict()
person['name'] = str(input('Name: ')).strip().capitalize()
yearbirth = int(input('Year of birth: '))
person['age'] = (datetime.date.today().year - yearbirth)
ctps = int(input('Do you have CTPS? (Type 0 if you do not have) '))
if ctps == 0:
	print('-='*30)
	for key, value in person.items():
		print(f'	The {key} is {value}.')
	print('	Does not have CTPS.')
else:
	person['CTPS'] = ctps
	person['salary'] = float(input('What is your salary? '))
	person['year of hiring'] = int(input('Wich year you were hired? '))
	yearsworked = (datetime.date.today().year - person['year of hiring'])
	if yearsworked < 35:
		person['retirement'] = (35 - yearsworked) + person['age']
	else:
		person['retirement'] = 'You can enjoy your retirement'
	print('-='*30)
	for key, value in person.items():
		print(f'	The {key} is {value}.')
print('-='*30)
