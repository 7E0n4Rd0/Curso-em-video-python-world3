# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.items())
# del pessoas['sexo']
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 98.5
"""for k, v in pessoas.items():
    print(f'O {k} = {v}')"""

"""brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])"""

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Para fazer isto tem que usar o método .copy()
# print(brasil)  Pois não tem como fazer o fatiamento '[:]' 
"""for state in brasil:
    for key, value in state.items():
        print(f'O campo {key} tem valor {value}.')"""
for state in brasil:
    for value in state.values():
        print(value)