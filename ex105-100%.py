# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
# vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*grades, status=False):
    """
    Function that takes students grades, calculates the medium grade of the class, 
    show the higher and lower grade and, optional, the class status.
    :param *grades: grab any grade inside the function;
    :param status: a boolean parammeter that is optional to show the class status.
    return: a dictionary with the data
    """
    s = float()
    global situation
    for value in range(0, len(grades)):
        if value == 0:
            higher_grade = grades[value]
            lower_grade = grades[value]
        else:
            if grades[value] > higher_grade:
                higher_grade = grades[value]
            elif grades[value] < lower_grade:
                lower_grade = grades[value]
        s += float(grades[value])
    
    medium = float(s/len(grades))
    if medium < 5.5:
        situation = str('BAD')
    elif medium >= 6:
        situation = str('REASONABLE')
    elif medium > 7:
        situation = str('GOOD')

    if status == False:
        report = {'Total of grades: ':len(grades), 'The higher grade was: ':higher_grade, 'The lower grade was: ':lower_grade,
                   'The medium was: ':f'{medium:.2f}'}
    else:
       report = {'Total of grades: ':len(grades), 'The higher grade was: ':higher_grade, 'The lower grade was: ':lower_grade,
                   'The medium was: ':f'{medium:.2f}' , 'Status: ':situation}
    return report


answer = notas(5.5, 9.5, 10, 6.5, status=True)
print(answer)
