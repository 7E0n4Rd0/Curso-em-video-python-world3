# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.error
import urllib.request

def verify_pudim():
    try:
        pudim = urllib.request.urlopen("https://www.pudim.com.br")
        print('\033[32mI could acess the website "pudim.com.br"\033[m')
    except urllib.error.URLError:
        print(f'\033[31mI could not acess the website "pudim.com.br".\033[m')


verify_pudim()
