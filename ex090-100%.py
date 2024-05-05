# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

student = {}
student['name'] = str(input('Name: ')).capitalize().strip()
student['media'] = float(input(f'Media of {student["name"]}: '))
if student['media'] >= 7:
    student['situation'] = 'Approved!'
elif student['media'] < 5:
    student['situation'] = 'Reproved!'
else:
    student['situation'] = 'Recuperation!'
print('-='*20)
for key, values in student.items():
    print(f'The {key} is {values}')
