import math

from utils.input import intInput

def ex6() -> None:
	"""
	Exercice 6: Calcul du logarithme népérien, sinus et cosinus d'un nombre entré par l'utilisateur.
	:return: None
	:rtype: None
	"""
	number: int = intInput(1)
	print(f"""
Nombre originel : {number}
Logarithme népérien log(n) : {math.log(number)}
Sinus sin(n) : {math.sin(number)}
Cosinus cos(n) : {math.cos(number)}
""")