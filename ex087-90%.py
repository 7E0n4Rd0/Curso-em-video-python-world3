# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados;
# b) A soma dos valores da terceira coluna;
# c) O maior valor da segunda linha.

array = [[], [], []]
allpair = allthirdcolumn = highersecondline = 0
for i in range(0, 3): # Line
    for j in range(0, 3): # Column
        number = int(input(f'Type a number in position [{i}][{j}]: ' ))
        if number % 2 == 0:
            allpair += number
        array[i].append(number)
    """if array[0][2]:
        allthirdcolun += number
    elif array[1][2]: #The way that I used.
        allthirdcolun += number
    elif array[2][2]:
        allthirdcolun += number
    else:
        allthirdcolun += 0"""    
print('<=>'*20)
for i in range(0, 3):
    allthirdcolumn += array[i][2]
    for j in range(0, 3):
        """if array[1][0] > highersecondline:
            highersecondline = array[1][0] # The way that I used.
        elif array[1][1] > highersecondline:
            highersecondline = array [1][1]
        elif array[1][2] > highersecondline:
            highersecondline = array[1][2]"""
        if j == 0:
            highersecondline = array[1][j]
        elif array[1][j] > highersecondline:
            highersecondline = array[1][j]
        print(f'[ {array[i][j]:^5} ]', end='')
    print()
print(f'The sum of all pair numbers are: {allpair}')
print(f'The sum of all third colun numbers are: {allthirdcolumn}')
print(f'The higher number in the second line is {highersecondline}')