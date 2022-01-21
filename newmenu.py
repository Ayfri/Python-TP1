from typing import Callable
from utils.prints import Color, print_line

exercices: list[str] = [
	'Types prédéfinis',
	'Calcul d’une surface',
	'Somme',
	'Factorielle',
	'Table de multiplications',
	'Saisie de nombres et de caractères',
	'Calcul de crédit'
]

def openExercice(number: int) -> None:
	"""
	Ouvre un exercice en fonction de son numéro.
	:param number: Le numéro de l'exercice à ouvrir.
	:type number: int
	:return: None
	:rtype: None
	"""
	module: object = __import__(f"src.ex{number}")
	subModule: object = getattr(module, f"ex{number}")
	function: Callable = getattr(subModule, f"tp{number}")
	function()

def terminalMenu() -> None:
	"""
	Affiche le menu principal du terminal.
	:return: None
	:rtype: None
	"""
	list = '\n'.join(f"Exercice {i} : {exercices[i - 1]}" for i in range(1, 8))
	print_line("Menu")
	print(f"""{list}
	
STOP pour arrêter.
""")

def main() -> None:
	"""
	Fonction principale du programme.
	Affiche le menu de sélection des exercices.
	:return: None
	:rtype: None
	"""
	print(f"{Color.RED}Bienvenue dans le menu du TP 1")
	while True:
		terminalMenu()
		input1: str = input("Veuillez choisir un exercice à réaliser : ")
		if input1.lower() == "stop":
			print("Au revoir :)")
			break
		elif input1.isdigit() and int(input1) in range(1, 7):
			print(f"Lancement de l'exercice n°{input1}")
			print_line(f"Exercice n°{input1}")
			openExercice(int(input1))
			print("Tapez ENTRER pour revenir dans le menu.")
			input()
		else:
			print("Veuillez entrer un nombre entre 1 et 7")

if __name__ == "__main__":
	main()
