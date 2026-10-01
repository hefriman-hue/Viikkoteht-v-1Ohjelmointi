hinta=float(input("anna hinta ilman alv"))
hinta_alv =hinta * 1.24
print(f"hinta alv:n kanssa: {hinta_alv:.2f} €")


matka=float(input("anna matkan pituus"))
kulutus = matka / 100 * 6.5
print (f"kulutus: {kulutus:.1f}")


minuutit = int(input("anna minuutit:"))
tunnit= minuutit// 60
minuutit= minuutit% 60
print(f"{tunnit}tuntia ja{minuutit}minuuttia")










