from typing import Callable
from utils.prints import Color, print_line

exercises: list[str] = [
	'Types prédéfinis',
	'Calcul d’une surface',
	'Somme',
	'Factorielle',
	'Table de multiplications',
	'Saisie de nombres et de caractères',
	'Calcul de crédit'
]

def open_exercice(number: int) -> None:
	"""
	Ouvre un exercice en fonction de son numéro.

	:param number: Le numéro de l'exercice à ouvrir.
	:type number: int
	:return: None
	:rtype: None
	"""
	module: object = __import__(f"src.ex{number}")
	sub_module: object = getattr(module, f"ex{number}")
	function: Callable = getattr(sub_module, f"ex{number}")
	function()

def print_terminal_menu() -> None:
	"""
	Affiche le menu principal du terminal.

	:return: None
	:rtype: None
	"""
	exercises_list: str = '\n'.join(f"Exercice {Color.CYAN}{i}{Color.END} : {Color.GREEN}{exercises[i - 1]}{Color.END}" for i in range(1, 8))
	print_line("Menu", color = Color.YELLOW)
	print(f"{exercises_list}\n\n{Color.RED}STOP pour arrêter.{Color.END}")

def main() -> None:
	"""
	Fonction principale du programme.
	Affiche le menu de sélection des exercices.

	:return: None
	:rtype: None
	"""
	print(f"{Color.RED}Bienvenue dans le menu du TP 1{Color.END}")
	while True:
		print_terminal_menu()
		try:
			input1: str = input(f"{Color.BLUE}Veuillez choisir un exercice à réaliser : {Color.END}")
			if input1.lower() == "stop":
				raise KeyboardInterrupt
			elif input1.isdigit() and int(input1) in range(1, 8):
				print(f"Lancement de l'exercice n°{input1}")
				print_line(f"Exercice n°{input1}", color = Color.YELLOW)
				open_exercice(int(input1))
				print("\nTapez ENTRER pour revenir dans le menu.")
				input()
			else:
				print(f"{Color.YELLOW}Veuillez entrer un nombre entre 1 et 7.{Color.END}")
		except Exception:
			print(f"{Color.CYAN}Au revoir :){Color.END}")
			exit(1)

if __name__ == "__main__":
	main()
