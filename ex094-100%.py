# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas;
# b) A média de idade do grupo;
# c) Uma lista com todas as mulheres;
# d) Uma lista com todas as pessoas com idade acima da média.

peoplecounter = sumage = mediage = 0
people = list()
women = list()
olderthanmedia = list()
person = dict()
while True:
	person['name'] = str(input('Name: ')).strip().capitalize()
	person['age'] = int(input('Age: '))
	person['sex'] = str(input('Sex: ')).strip().upper()[0]
	while person['sex'] not in 'MmFf':
		print('Error, please enter only M or F!!')
		person['sex'] = str(input('Sex: ')).strip().upper()[0]
	people.append(person.copy())
	person.clear()
	answer = str(input('Do you want to continue? [Y/N] ')).strip()[0]
	while answer not in 'YyNn':
		print('Error, please enter only Y or N!!')
		answer = str(input('Do you want to continue? [Y/N] ')).strip()[0]
	if answer in 'Nn':
		peoplecounter += 1
		break
	else:
		peoplecounter += 1
		print('-='*20)
print('-='*30)
for i in range(0, len(people)):
	for key, value in people[i].items():
		if key in 'age':
			sumage += value
		if key in 'sex' and value in 'Ff':
			women.append(people[i]['name'])
mediage = (sumage/peoplecounter)
print(f'{peoplecounter} people were registered.')
print(f'Age media is : {mediage:.2f}')
print('Registered women: ',women)
for i in range(0, len(people)):
	for key, value in people[i].items():
		if key in 'age' and value > mediage:
			for k, v in people[i].items():
				olderthanmedia.append(people[i][k])
print(f'People who is older than the media age: {olderthanmedia}')
print('-='*30)
