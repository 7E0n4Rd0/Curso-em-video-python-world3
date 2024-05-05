# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(message):
    print('='*(len(message)+2))
    print(f' {message}')
    print('='*(len(message)+2))

# Main code
escreva("Olá, mundo!")
escreva("Curso de Python no Youtube")
escreva("CeV") 
escreva("Leonardo")