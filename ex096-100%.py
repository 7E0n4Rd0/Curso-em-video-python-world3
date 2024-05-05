# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(width, lenght):
    area = width*lenght
    print(f'The area of the land {width}x{lenght} is {area:.1f}m²') 

# Main code
width = float(input("Type the width of the land (m): "))
lenght = float(input("Type the lenght of the land (m): "))
área(width, lenght)