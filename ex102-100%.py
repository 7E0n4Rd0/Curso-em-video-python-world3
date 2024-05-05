# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro 
# que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será 
# mostrado ou não na tela o processo de cálculo do fatorial.
import time

def fatorial(n, show=False):
	"""
	-> Calculates the factorial of a number
	:param n: The number to be calculate
	:param show: (optional) Show or not the process
	:return: The value of the factiorial by n.
	"""
	counter = n
	factorial = 1
	if(show):
		while(counter > 0):
			print(f'{counter}','x' if(counter >1) else '=' ,end=' ', flush=True)
			time.sleep(0.5)
			factorial *= counter
			counter -= 1
		print(factorial)
		print(f'The factorial of {n} is {factorial}.')
	else:
		while(counter > 0):
			factorial *= counter
			counter -= 1
		print(f'The factorial of {n} is {factorial}.')
		

number = int(input('Enter a number to calculate the factorial: '))
answer = str(input('Do you want to show the process of calculus: ')).capitalize().strip()
while(answer not in 'YN'):
	print('Error')
	answer = str(input('Do you want to show the process of calculus [Y/N]: ')).capitalize().strip()
	
if(answer == 'Y'):
	fatorial(number, True)
else:
	fatorial(number, False)
