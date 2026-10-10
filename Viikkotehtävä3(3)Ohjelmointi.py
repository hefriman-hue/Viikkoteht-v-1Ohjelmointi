tunnit=float(input("Syötä viikon työtunnit:"))
tuntipalkka=float(input("Syötä tuntipalkkasi:"))
if tunnit <= 40:
    palkka = tunnit*tuntipalkka
else:
    ylityötunnit= tunnit -40
    palkka = 40 * tuntipalkka + ylityötunnit * tuntipalkka * 1.5
print(f"Viikon ansiosi ovat: {palkka:.2f}€")