tyyppi = input("Valitse lähetys (1= kirje, 2 = paketti):").strip()
paino =int(input("Anna paino grammoina:"))
if paino <= 0:
    print("Painon täytyy olla suurempi kuin 0.")
elif tyyppi !="1"and tyyppi !="2":
    print(" tuntematon lähetystyyppi.")
else:
    sadat =paino//100

    if tyyppi == "1":
        hinta =50 # Hinta sentteinä

        if paino < 200:
            pass
        elif paino <= 500:
            hinta = hinta + sadat * 4
        else:
            hinta = hinta + sadat * 7
            mahtuu = input(" Mahtuuko kirje postilaatikkoon? (k/e):")
            if mahtuu =="e":
                hinta =hinta + 200

    else:
        hinta =200 # Paketin perushinta sentteinä

        if paino < 200:
            pass
        elif paino <= 500:
            hinta = hinta + sadat * 14
    print (f"Lähetyksen hinta: {hinta / 100:2f}€")
