from utils.input import charInput, intInput

def ex1() -> None:
	"""
	Exercice 1 : Afficher un caractère et un nombre entier entrés par l'utilisateur.
	:return: None
	:rtype: None
	"""
	char: chr = charInput()
	number: int = intInput()
	print(f"""Vous avez entré : {char} et {str(number)}
L'index du caractère est {ord(char)} et le nombre en tant que caractère est {chr(number)}""")
