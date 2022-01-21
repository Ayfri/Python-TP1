import sys

from utils.input import intInput

def ex3() -> None:
    """
    Exercice 3 : Calculer la somme de 1 + 2 + 3 + ... + n.
    :return: None
    :rtype: None
    """
    number: int = intInput(1, lambda i: (i * (i + 1)) / 2)
    bigResult: int = int((number * (number + 1)) / 2)
    additionString: str = ' '.join([f'{i} +' for i in range(1, number)]) + ' ' + str(number)
    print(f"""
    La somme du nombre {number} et des inférieurs jusqu'à 1 est {bigResult}
    {additionString} = {bigResult}
    {bigResult} = {additionString}""")