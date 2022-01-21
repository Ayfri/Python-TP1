import math
import sys
from typing import Callable

from utils.prints import Color

def int_input(
		min_nbr: int = -sys.maxsize,
		max_nbr: Callable[[int], int] = lambda i: sys.maxsize,
		text: str = "Rentrez un nombre : "
) -> int:
	"""
	Permet de demander un nombre entier à l'utilisateur.

	:param min_nbr: Le nombre minimum à rentrer.
	:type min_nbr: int
	:param max_nbr: Le nombre maximum à rentrer.
	:type max_nbr: Callable[[int], int] | None
	:param text: Le texte à afficher pour demander le nombre.
	:type text: str
	:return: Le nombre entier saisi par l'utilisateur.
	:rtype: int
	"""
	result: int
	while True:
		input1: str = input(text)
		try:
			result = int(input1)
			max_result: int = max_nbr(result)
			if result < min_nbr:
				print(f"{Color.YELLOW}Le nombre est trop petit, il doit être au dessus de {min_nbr - 1}{Color.END}")
				continue
			if result > max_result:
				print(f"{Color.YELLOW}Le nombre est trop grand, il doit être en dessous de {max_result}.{Color.END}")
				continue
			break
		except ValueError:
			print(f"{Color.YELLOW}Nombre invalide.{Color.END}")

	return result

def char_input() -> chr:
	"""
	Permet de demander un caractère à l'utilisateur.

	:return: Le caractère saisi par l'utilisateur.
	:rtype: chr
	"""
	result: chr
	while True:
		input1: str = input("Rentrez un caractère : ")
		try:
			if len(input1) != 1:
				print(f"{Color.YELLOW}Veuillez saisir un seul caractère.{Color.END}")
				continue
			result = input1
			break
		except ValueError:
			print(f"{Color.YELLOW}Caractère invalide.{Color.END}")

	return result

def float_input(text: str = "Saisissez un nombre : ") -> float:
	"""
	Permet de demander un nombre à virgule à l'utilisateur.

	:param text: Le texte à afficher pour demander le nombre.
	:type text: str
	:return: Le nombre flottant saisi par l'utilisateur.
	:rtype: float
	"""
	result: float
	while True:
		input1: str = input(text)
		try:
			result = float(input1)
			if (result * result) > sys.maxsize:
				print(f"{Color.YELLOW}Veuillez saisir un nombre inférieur à {sys.maxsize}.{Color.END}")
			if result < 0:
				print(f"{Color.YELLOW}Le nombre doit être positif.{Color.END}")
				continue
			break
		except ValueError:
			print(f"{Color.YELLOW}Nombre invalide.{Color.END}")
		except OverflowError:
			print(f"{Color.YELLOW}Veuillez saisir un nombre inférieur à {math.sqrt(result)}.{Color.END}")

	return result
