try:
    luku1=float(input("Anna ensimmäinen numero:"))
    luku2 = float(input("Anna toinen numero:"))
    tulos =luku1/luku2
    print(tulos)
except ValueError:
    print("Virheellinen muoto.")
except ZeroDivisionError:
    print("Nollalla ei saa jakaa.")

