from utils.input import float_input

def ex7() -> None:
	"""
	Exercice 7: Calculer le taux de crédit mensuel d'un prêt sur plusieurs années avec un taux d'intérêts fixes.
	:return: None
	:rtype: None
	"""
	totalDebt = float_input("Saisissez le montant de votre dette : ")
	totalYears = float_input("Saisissez le nombre d'années que vous avez dépensé pour payer votre dette : ")
	annualRate = float_input("Saisissez le taux d'intérêt annuel : ")
	monthRate = ((annualRate / 100) / 12)
	monthTotal = (totalYears * 12)
	monthlyPayment = totalDebt * monthRate * (((1 + monthRate) ** monthTotal) / ((1 + monthRate) ** monthTotal - 1))
	print(f"Mensualités = {monthlyPayment:.2f}€")
