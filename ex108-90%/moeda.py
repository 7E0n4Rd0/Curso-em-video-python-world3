def aumentar(number=0.0, value=0):
	"""
	:param number: the number to get increase.
	:param value: the value in percent of the increase.
	return: number increased.
	"""
	return number + (number*value/100)


def diminuir(number=0.0, value=0): 
	"""
	:param number: the number to get decrease.
	:param value: the value in percent of the decrease.
	return: number decreased.
	"""
	return number - (number*value/100)


def dobro(number=0.0):
	"""
	:param number: the number to get multiply.
	return: number multiplied by two.
	"""
	return number*2


def metade(number=0.0):
	"""
	:param number: the number to get divide.
	return: number divided by two.
	"""
	return number/2


def moeda(number=0.0, moeda='R$'):
	return f'{moeda}{number:.2f}'.replace('.',',')

# I didn't saw that was obligated to replace the dot to the virgule.