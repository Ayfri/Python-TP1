import math

from utils.input import int_input
from utils.prints import Color

def ex6() -> None:
	"""
	Exercice 6: Calcul du logarithme népérien, sinus et cosinus d'un nombre entré par l'utilisateur.

	:return: None
	:rtype: None
	"""
	number: int = int_input(1)
	print(f"""{Color.PURPLE}Nombre originel : {number}
Logarithme népérien log(n) : {math.log(number)}
Sinus sin(n) : {math.sin(number)}
Cosinus cos(n) : {math.cos(number)}{Color.END}""")
