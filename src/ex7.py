from utils.input import float_input
from utils.prints import Color

def ex7() -> None:
	"""
	Exercice 7: Calculer le taux de crédit mensuel d'un prêt sur plusieurs années avec un taux d'intérêts fixes.

	:return: None
	:rtype: None
	"""
	total_debt: float = float_input("Saisissez le montant de votre dette : ")
	total_years: float = float_input("Saisissez le nombre d'années que vous avez dépensé pour payer votre dette : ")
	annual_rate: float = float_input("Saisissez le taux d'intérêt annuel : ")
	month_rate: float = ((annual_rate / 100) / 12)
	month_total: float = (total_years * 12)
	monthly_payment: float = total_debt * month_rate * (
				((1 + month_rate) ** month_total) / ((1 + month_rate) ** month_total - 1))
	print(f"{Color.PURPLE}Mensualités = {monthly_payment:.2f}€{Color.END}")

if __name__ == "__main__":
	ex7()
