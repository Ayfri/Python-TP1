import math

from utils.input import int_input
from utils.prints import Color

def ex4() -> None:
	"""
	Exercise 4: Calculer la factorielle d'un nombre entré par l'utilisateur.

	:return: None
	:rtype: None
	"""
	number: int = int_input(min_nbr = 1, max_nbr = math.factorial)
	big_result: int = math.factorial(number)
	addition_string: str = ' '.join([f'{i} ×' for i in range(1, number)]) + ' ' + str(number)
	print(f"""{Color.PURPLE}La factorielle de {number}, notée 8!, et vaut :
	{addition_string} = {big_result}
	{big_result} = {addition_string}{Color.END}""")