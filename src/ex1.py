from utils.input import char_input, int_input

def ex1() -> None:
	"""
	Exercice 1 : Afficher un caractère et un nombre entier entrés par l'utilisateur.
	:return: None
	:rtype: None
	"""
	char: chr = char_input()
	number: int = int_input()
	print(f"""Vous avez entré : {char} et {str(number)}
L'index du caractère est {ord(char)} et le nombre en tant que caractère est {chr(number)}""")
