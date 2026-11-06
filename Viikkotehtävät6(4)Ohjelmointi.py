tilaukset = [
    "T1565_2020",
    "T2432_2019",
    "T8551_2018",
    "T3342_2019",
    "T9814_2018",
    "T7733_2020"
    ]
vuosi =input("Anna vuosiluku:")
for tilaus in tilaukset:
    koodi,vuosiluku = tilaus.split("_")
    if vuosiluku == vuosi:
        print(koodi)
