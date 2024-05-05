# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o 
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: 
# use cores.

from time import sleep

colors = {'clean':'\033[m','red': '\033[37;41m', 'green': '\033[37;42m', 'blue': '\033[37;44m'}

def messages(text, color=colors["clean"],line=False):
    if line:
        print(f'{color}~{colors["clean"]}'*(len(text)+2))
        print(f'{color} {text} {colors["clean"]}')
        print(f'{color}~{colors["clean"]}'*(len(text)+2),end='', flush=True)
        sleep(1)
    else:
        print(colors["green"])
        print(help(text))
        print(colors["clean"])
        sleep(2)

def interactiveHelp():
    while True:
        messages('Interactive Help', colors["blue"],line=True)
        answer = str(input('\n>>> '))
        if (answer in 'FIMfim' or answer in 'ENDend'):
            messages('Good bye', colors["red"], line=True)
            sleep(1)
            break
        else:
            messages(f'Searching for the doc of {answer}' ,colors["red"],line=True)
            messages(answer)


# Main code
interactiveHelp()
