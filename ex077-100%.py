# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.
words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro')
c = 0
while True:
    word = words[c]
    print(f'\nIn the word {word.upper()} we have: ', end='')
    for a in range(0, len(word)):
        if word[a] in 'aeiou':
            print(word[a], end=' ')
    c += 1
    if c == 12:
        break
    # I could use to for structures - 11:56 - 06/03/2023
# for c in words:
#   print(f'\nIn the word {word.upper()} we have: ', end='')
#   for letter in c:
#       if letter.lower() in 'aeiou':
#           print(letter, end=' ')
