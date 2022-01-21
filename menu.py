from typing import Callable

from utils.prints import Color, print_line

exercises: dict[str, str] = {
	'Types prédéfinis': """
• Écrire un script permettant de rentrer 1 caractères et un entier.
• Afficher la variables sous forme d'entiers et de caractères.""",
	'Calcul d’une surface': """Écrire un programme qui calcule la surface d’un trapèze.""",
	'Somme': """Écrire un algorithme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu’à ce nombre.""",
	'Factorielle': """Écrire un algorithme qui demande un nombre de départ, et qui calcule sa factorielle.""",
	'Table de multiplications': """Écrire un algorithme qui demande un nombre de départ, et qui ensuite écrit la table de multiplication de ce nombre.""",
	'Saisie de nombres et de caractères': """Écrire un script permettant de saisir un entier au clavier et d’afficher :
• Le logarithme népérien de l’entier
• Le sinus de l’entier
• Le cosinus de l’entier""",
	'Calcul de crédit': """Écrivez l’algorithme qui calcule la mensualité d’un crédit immobilier à taux fixe.
Il demandera le montant du capital emprunté, le nombre d’années et le taux annuel.""",
}

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
	exercises_list: str = '\n'.join(
		f"Exercice {Color.CYAN}{i}{Color.END} : {Color.GREEN}{list(exercises.keys())[i - 1]}{Color.END}" for i in
		range(1, 8))
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
				print(f"Consigne: {list(exercises.values())[int(input1) - 1]}\n")
				open_exercice(int(input1))
				print("\nTapez ENTRER pour revenir dans le menu.")
				input()
			else:
				print(f"{Color.YELLOW}Veuillez entrer un nombre entre 1 et 7.{Color.END}")
		except:
			print(f"{Color.CYAN}Au revoir :){Color.END}")
			exit(1)

if __name__ == "__main__":
	main()
