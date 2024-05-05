def aumentar(number=0.0, value=0, formate=False):
	"""
	:param number: the number to get increase.
	:param value: the value in percent of the increase.
	:param formate: it's a boolean parameter that formats the value.
	return: number increased and number formated if parameter format is True.
	"""
	if formate:
		return moeda(number + (number*value/100))
	else:	
		return number + (number*value/100)


def diminuir(number=0.0, value=0, formate=False): 
	"""
	:param number: the number to get decrease.
	:param value: the value in percent of the decrease.
	:param formate: it's a boolean parameter that formats the value.
	return: number decreased and number formated if parameter format is True.
	"""
	if formate:
		return moeda(number - (number*value/100))
	else:
		return number - (number*value/100)


def dobro(number=0.0, formate=False):
	"""
	:param number: the number to get multiply.
	:param formate: it's a boolean parameter that formats the value.
	return: number multiplied by two and number formated if parameter format is True.
	"""
	if formate:
		return moeda(number*2)
	else:
		return number*2


def metade(number=0.0, formate=False):
	"""
	:param number: the number to get divide.
	:param formate: it's a boolean parameter that formats the value.
	return: number divided by two and number formated if parameter format is True.
	"""
	if format:
		return moeda(number/2)
	else:
		return number/2


def moeda(number=0.0, moeda='R$'):
	"""
	:param number: the number to get format.
	:param moeda: the type of coin.
	return: number formated
	"""
	return f'{moeda}{number:.2f}'.replace('.',',')


def resumo(number=0.0, x=0, y=0):
	"""
	:param number: the value of the price.
	:param x: value to be a parameter of the call aumentar().
	:param y: value to be a parameter of the call diminuir().
	return: a text block formated with the data.
	"""
	print(f"""-------------------------------------------
            Resume of the Value
-------------------------------------------
The price analysed: \t{moeda(number)}
Half of price is: \t{metade(number, True)}
Double of the price is: {dobro(number, True)}
Increasing {x}%: \t{aumentar(number, x, True)}
Reducing {y}%: \t\t{diminuir(number, y, True)}
-------------------------------------------""")
