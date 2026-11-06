numerot = [
    "nolla",
    "yksi",
    "kaksi",
    "kolme",
    "neljä",
    "viisi",
    "kuusi",
    "seitsemän",
    "kahdeksan",
    "yhdeksän"
]
luku =input("Anna enintään viisinumeroinen luku:")
if len(luku)>5 or not luku.isdigit():
    print ("Anna enintään viisinumeroinen luku:")
else :
    for numero in luku :
        print (numerot[int(numero)], end="")


