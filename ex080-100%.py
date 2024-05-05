#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e 
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

values = []
values.append(int(input("Type the first number: ")))
values.insert(1, int(input('Type the second number: ')))
values.insert(2, int(input('Type the third number: ')))
values.insert(3, int(input('Type the fourth number: ')))
values.insert(4, int(input('Type the fith number: ')))
print("Values that the user typed: ", values)

# Position 0
if(values[0] > values[1]): 
    hand = values[0]
    values[0] = values[1]
    values[1] = hand
    
if (values[0] < values[1] and values[0] > values[2]):
    hand = values[0]
    values[0] = values[2]
    values[2] = hand
    
if (values[0] < values[1] and values[0] < values[2] and values[0] > values[3]):
    hand = values[0]
    values[0] = values[3]
    values[3] = hand
    
if (values[0] < values[1] and values[0] < values[2] and values[0] < values[3] and values[0] > values[4]):
    hand = values[0]
    values[0] = values[4]
    values[4] = hand

# Position 1
if(values[1] < values[0]):
    hand = values[0]
    values[0] = values[1]
    values[1] = hand
    
if(values[1] > values[0] and values[1] > values[2]):
    hand = values[1]
    values[1] = values[2]
    values[2] = hand
    
if(values[1] > values[0] and values[1] < values[2] and values[1] > values[3]):
    hand = values[1]
    values[1] = values[3]
    values[3] = hand
    
if(values[1] > values[0] and values[1] < values[2] and values[1] < values[3] and values[1] > values[4]):
    hand = values[1]
    values[1] = values[4]
    values[4] = hand
    
# Position 2
if(values[2] < values[0]):
    hand = values[0]
    values[0] = values[2]
    values[2] = hand
    
if(values[2] < values[1]):
    hand = values[1]
    values[1] = values[2]
    values[2] = hand
    
if(values[2] > values[1] and values[2] > values[3]):
    hand = values[2]
    values[2] = values[3]
    values[3] = hand
    
if(values[2] < values[3] and values[2] > values[1] and values[2] > values[4]):
    hand = values[2]
    values[2] = values[4]
    values[4] = hand
    
# Position 3
if(values[3] < values[0]):
    hand = values[0]
    values[0] = values[3]
    values[3] = hand
    
if(values[3] < values[1]):
    hand = values[1]
    values[1] = values[3]
    values[3] = hand
    
if(values[3] < values[2]):
    hand = values[2]
    values[2] = values[3]
    values[3] = hand
    
if(values[3] > values[2] and values[3] > values[4]):
    hand = values[3]
    values[3] = values[4]
    values[4] = hand
    
if(values[3] > values[2] and values[3] < values[4] and values[1] > values[3]):
    hand = values[1]
    values[1] = values[3]
    values[3] = hand
    
if(values[3] > values[0] and values[3] > values[1] and values[2] > values[3]):
    hand = values[2]
    values[2] = values[3]
    values[3] = hand
    
# Position 4
if(values[4] < values[0]):
    hand = values[0]
    values[0] = values[4]
    values[4] = hand
    
if(values[4] < values[1]):
    hand = values[1]
    values[1] = values[4]
    values[4] = hand
    
if(values[4] < values[2]):
    hand = values[2]
    values[2] = values[4]
    values[4] = hand
    
if(values[4] < values[3]):
    hand = values[3]
    values[3] = values[4]
    values[4] = hand
    
print("Values in order: ", values)
# It was written in the website that "Orderned List without loop" and the teacher used for and while to do this. I fell idiot now.