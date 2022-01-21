from enum import Enum

def print_line(text = '', length=40) -> None:
	"""
	Écrit dans la console une ligne de texte de longueur length avec un texte au milieu si nécessaire.
	:param text: Le texte au milieu à afficher si nécessaire.
	:type text: str
	:param length: La longueur de la ligne à afficher.
	:type length: int
	:return: None
	:rtype: None
	"""
	if len(text) > 0:
		text = f" {text} "
	print('-' * int(length / 2) + text + '-' * int(length / 2))

class Color(Enum):
	RED: str ='\033[91m'
	GREEN: str ='\033[92m'
	YELLOW: str ='\033[93m'
	BLUE: str ='\033[94m'
	PURPLE: str='\033[95m'
	CYAN: str='\033[96m'
	WHITE: str='\033[97m'
	END: str='\033[0m'