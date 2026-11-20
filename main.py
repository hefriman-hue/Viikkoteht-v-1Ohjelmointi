from tkinter import messagebox

from functions import *
amount = float(input("Anna rahasumma:"))
from_currency = input("Anna alkuperäinen valuutta (€,$,£,kr):")
to_currency = input("Mihin valuuttaan muutetaan (€, $, £, kr):")
if from_currency in ["€", "$","£","kr"] and to_currency in ["€","$","£","kr"]:
    result = convert_money(amount, from_currency, to_currency)
    print(f" Muunnettu summa: {result:.2f}{to_currency}")
else:
    print("Virheellinen valuutta!")






