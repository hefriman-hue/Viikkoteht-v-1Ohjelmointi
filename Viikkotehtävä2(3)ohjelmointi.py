palkka= float(input("Anna kuukausipalkkasi:"))
Veroprosentti=float(input("Anna veroprosenttisi"))
vero=palkka * Veroprosentti /100
palkka=float(input("Anna kuukausipalkkasi:"))
Veroprosentti=float(input("Anna veroprosenttisi:"))
Vero=palkka*Veroprosentti/100
Kateen=palkka-vero
print("Veroihin menee", vero, "euroa")
print("käteen jää", Kateen, "euroa")
