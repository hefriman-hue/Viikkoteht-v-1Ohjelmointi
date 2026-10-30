import math
while True:
    sade = float(input("Anna säde:"))
    pinta_ala = math.pi* sade ** 2
    print( f"Ympyrän pinta-ala: {pinta_ala:.2f}")
    jatka=input("Haluatko jatkaa?  ( k/e)")
    if jatka == "e":
        break
