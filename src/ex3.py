from utils.input import int_input
from utils.prints import Color

def ex3() -> None:
	"""
	Exercice 3 : Calculer la somme de 1 + 2 + 3 + ... + n.

	:return: None
	:rtype: None
	"""
	number: int = int_input(1, lambda i: (i * (i + 1)) / 2)
	big_result: int = int((number * (number + 1)) / 2)
	addition_string: str = ' '.join([f'{i} +' for i in range(1, number)]) + ' ' + str(number)
	print(f"""{Color.PURPLE}La somme du nombre {number} et des inférieurs jusqu'à 1 est {big_result}
	{addition_string} = {big_result}
	{big_result} = {addition_string}{Color.END}""")
