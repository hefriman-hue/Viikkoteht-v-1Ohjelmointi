lampotila = int(input("Syötä päivän lämpötila:"))
if 0 <= lampotila <= 10:
    print("KYLMÄÄ")
elif 11 <= lampotila <= 15:
    print ("KOLEAA")
elif 16 <= lampotila <= 20:
    print("MELKO LÄMMINTÄ")
elif 21 <= lampotila <= 25:
    print(" LÄMMINTÄ")
elif 26 <= lampotila <= 30:
    print("HELLETTÄ")
else:
    print("Lämpötila on tehtävän alueen 0-30 ulkopuolella")