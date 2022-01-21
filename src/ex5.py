from utils.input import int_input

def ex5() -> None:
	"""
	Exercise 5: Afficher la table de multiplication de l'entier saisi.
	:return: None
	:rtype: None
	"""
	number: int = int_input(1, lambda x: x * 10)
	table: str = '\n'.join([f'- {number} x {i} = {number * i}' for i in range(1, 11)])
	print(f"""Table de {number} : {table}""")