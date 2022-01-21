import math
import sys

from utils.input import intInput

def ex4() -> None:
	"""
	Exercise 4: Calculer la factorielle d'un nombre entré par l'utilisateur.
	:return: None
	:rtype: None
	"""
	number: int = intInput(min_nbr = 1, max_nbr = math.factorial)
	bigResult: int = math.factorial(number)
	additionString: str = ' '.join([f'{i} ×' for i in range(1, number)]) + ' ' + str(number)
	print(f"""
	La factorielle de {number}, notée 8!, et vaut :
	{additionString} = {bigResult}
	{bigResult} = {additionString}""")