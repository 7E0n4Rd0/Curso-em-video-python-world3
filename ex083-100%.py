# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

while True:
    countR = 0
    countL = 0
    expression = list(str(input("Type a math expression: ")))
    for index in range(0, len(expression)):
        if(expression[index] == '('):
            countL += 1
        if(expression[index] == ')'):
            countR += 1
    break

if(countL == countR):
    print("The expression is valid")
else:
    print("The expression is not valid")
        